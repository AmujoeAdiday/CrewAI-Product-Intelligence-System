from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class DataInput(BaseModel):
    """Input schema for data analysis tools."""
    data_path: str = Field(..., description="Path to the CSV data file")
    product_name: str = Field(..., description="Name of the product to analyze")

class SeasonalityAnalysisTool(BaseTool):
    name: str = "Seasonality Analysis Tool"
    description: str = (
        "Analyzes seasonal patterns in product sales data. "
        "Identifies peak months, low seasons, and calculates seasonality scores."
    )
    args_schema: Type[BaseModel] = DataInput

    def _run(self, data_path: str, product_name: str) -> str:
        """Execute seasonality analysis"""
        try:
            # Load data
            data = pd.read_csv(data_path)
            
            # Handle different column names
            product_col = 'Product_Name' if 'Product_Name' in data.columns else 'Product'
            sales_col = 'Weekly_Sales' if 'Weekly_Sales' in data.columns else 'Units_Sold'
            
            # Filter for specific product
            product_data = data[data[product_col] == product_name].copy()
            product_data['Date'] = pd.to_datetime(product_data['Date'])
            product_data['Month'] = product_data['Date'].dt.month
            
            # Calculate monthly averages
            monthly_avg = product_data.groupby('Month')[sales_col].mean()
            
            # Calculate seasonality metrics
            seasonal_strength = monthly_avg.std() / monthly_avg.mean()
            max_month = monthly_avg.max()
            min_month = monthly_avg.min()
            seasonality_score = (max_month - min_month) / monthly_avg.mean()
            
            # Identify peak and low months
            peak_months = monthly_avg.nlargest(3).index.tolist()
            low_months = monthly_avg.nsmallest(3).index.tolist()
            
            # Determine if seasonal
            is_seasonal = seasonality_score > 0.3
            
            result = f"""
SEASONALITY ANALYSIS FOR {product_name}:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Seasonality Score: {seasonality_score:.3f}
🌊 Seasonal Strength: {seasonal_strength:.3f}
🎯 Is Seasonal: {'YES' if is_seasonal else 'NO'}

📈 PEAK MONTHS: {', '.join([str(m) for m in peak_months])}
📉 LOW MONTHS: {', '.join([str(m) for m in low_months])}

💡 INSIGHTS:
{f'This product shows STRONG seasonal patterns!' if is_seasonal else 'This product has STABLE year-round demand.'}
Peak performance in months: {peak_months}
Consider inventory planning around these seasonal trends.
"""
            return result
            
        except Exception as e:
            return f"Error in seasonality analysis: {str(e)}"

class TrendAnalysisTool(BaseTool):
    name: str = "Trend Analysis Tool"
    description: str = (
        "Analyzes long-term trends in product sales data. "
        "Calculates trend slopes, R-squared values, and growth patterns."
    )
    args_schema: Type[BaseModel] = DataInput

    def _run(self, data_path: str, product_name: str) -> str:
        """Execute trend analysis"""
        try:
            # Load data
            data = pd.read_csv(data_path)
            
            # Handle different column names
            product_col = 'Product_Name' if 'Product_Name' in data.columns else 'Product'
            sales_col = 'Weekly_Sales' if 'Weekly_Sales' in data.columns else 'Units_Sold'
            
            # Filter for specific product
            product_data = data[data[product_col] == product_name].copy()
            product_data['Date'] = pd.to_datetime(product_data['Date'])
            product_data = product_data.sort_values('Date')
            
            # Prepare data for regression
            X = np.array(range(len(product_data))).reshape(-1, 1)
            y = product_data[sales_col].values
            
            # Fit linear regression
            model = LinearRegression()
            model.fit(X, y)
            
            slope = model.coef_[0]
            r_squared = model.score(X, y)
            
            # Calculate percentage change
            first_value = product_data[sales_col].iloc[0]
            last_value = product_data[sales_col].iloc[-1]
            total_change_pct = ((last_value - first_value) / first_value) * 100 if first_value > 0 else 0
            
            # Recent trend (last 12 weeks)
            if len(product_data) >= 12:
                recent_data = product_data.tail(12)
                X_recent = np.array(range(len(recent_data))).reshape(-1, 1)
                y_recent = recent_data[sales_col].values
                
                recent_model = LinearRegression()
                recent_model.fit(X_recent, y_recent)
                recent_slope = recent_model.coef_[0]
                recent_r_squared = recent_model.score(X_recent, y_recent)
            else:
                recent_slope = slope
                recent_r_squared = r_squared
            
            # Determine trend strength
            if r_squared > 0.7:
                strength = "STRONG"
            elif r_squared > 0.4:
                strength = "MODERATE"
            else:
                strength = "WEAK"
            
            # Determine direction
            if slope > 0.5:
                direction = "📈 RISING"
            elif slope < -0.5:
                direction = "📉 DECLINING"
            else:
                direction = "➡️ STABLE"
            
            result = f"""
TREND ANALYSIS FOR {product_name}:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Overall Trend: {direction}
📈 Slope: {slope:.3f} units/week
🎯 R-Squared: {r_squared:.3f}
💪 Trend Strength: {strength}

📅 RECENT PERFORMANCE (Last 12 weeks):
📈 Recent Slope: {recent_slope:.3f} units/week
🎯 Recent R²: {recent_r_squared:.3f}

📊 GROWTH METRICS:
🔢 Total Change: {total_change_pct:+.1f}%
📈 From {first_value:.0f} to {last_value:.0f} units

💡 STRATEGIC INSIGHT:
{f'Strong {direction.lower()} trend - high confidence predictions!' if strength == 'STRONG' else f'{strength.title()} trend - monitor closely for changes.'}
"""
            return result
            
        except Exception as e:
            return f"Error in trend analysis: {str(e)}"

class ProductClassificationTool(BaseTool):
    name: str = "Product Classification Tool"
    description: str = (
        "Classifies products into strategic categories based on trend and seasonality data. "
        "Categories include Rising Star, Seasonal Hero, Evergreen, Fading Out, etc."
    )
    args_schema: Type[BaseModel] = DataInput

    def _run(self, data_path: str, product_name: str) -> str:
        """Execute product classification"""
        try:
            # Load data
            data = pd.read_csv(data_path)
            
            # Handle different column names
            product_col = 'Product_Name' if 'Product_Name' in data.columns else 'Product'
            sales_col = 'Weekly_Sales' if 'Weekly_Sales' in data.columns else 'Units_Sold'
            
            # Get trend data
            product_data = data[data[product_col] == product_name].copy()
            product_data['Date'] = pd.to_datetime(product_data['Date'])
            product_data = product_data.sort_values('Date')
            
            # Calculate trend
            X = np.array(range(len(product_data))).reshape(-1, 1)
            y = product_data[sales_col].values
            model = LinearRegression()
            model.fit(X, y)
            slope = model.coef_[0]
            r_squared = model.score(X, y)
            
            # Calculate seasonality
            product_data['Month'] = product_data['Date'].dt.month
            monthly_avg = product_data.groupby('Month')[sales_col].mean()
            max_month = monthly_avg.max()
            min_month = monthly_avg.min()
            seasonality_score = (max_month - min_month) / monthly_avg.mean()
            is_seasonal = seasonality_score > 0.3
            
            # Classification logic
            if slope > 0.5 and r_squared > 0.5:
                classification = "🔥 RISING STAR"
                confidence = min(0.95, r_squared + (slope / 2))
                insight = "Strong upward trend! Consider increasing marketing investment and inventory."
            elif slope < -0.5 and r_squared > 0.5:
                classification = "💤 FADING OUT"
                confidence = min(0.95, r_squared + abs(slope) / 2)
                insight = "Declining trend detected. Consider product refresh or discontinuation."
            elif is_seasonal and abs(slope) < 0.3:
                classification = "💘 SEASONAL HERO"
                confidence = min(0.9, seasonality_score)
                insight = "Strong seasonal patterns! Plan inventory around peak months."
            elif not is_seasonal and abs(slope) < 0.3:
                classification = "🌲 EVERGREEN"
                confidence = 0.8 - seasonality_score
                insight = "Reliable, consistent performer. Great for steady revenue."
            elif r_squared < 0.3 and not is_seasonal:
                classification = "🎲 RANDOM/ERRATIC"
                confidence = 0.6
                insight = "Unpredictable patterns. Investigate external factors affecting sales."
            elif is_seasonal and slope < -0.2:
                classification = "📉 DECLINING SEASONAL"
                confidence = min(0.85, seasonality_score + abs(slope) / 3)
                insight = "Seasonal product losing steam. May need repositioning."
            else:
                classification = "📊 STABLE"
                confidence = 0.5
                insight = "Steady performance with no major trends."
            
            result = f"""
PRODUCT CLASSIFICATION FOR {product_name}:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏷️ CLASSIFICATION: {classification}
🎯 CONFIDENCE: {confidence:.0%}

📊 KEY METRICS:
📈 Trend Slope: {slope:.3f}
🎯 Trend R²: {r_squared:.3f}
🌊 Seasonality: {'YES' if is_seasonal else 'NO'} ({seasonality_score:.3f})

💡 STRATEGIC RECOMMENDATION:
{insight}

🎯 ACTION ITEMS:
• Monitor performance weekly
• Adjust inventory based on classification
• Consider marketing strategy alignment
"""
            return result
            
        except Exception as e:
            return f"Error in product classification: {str(e)}"