#!/usr/bin/env python3
"""
🎁 CrewAI Product Intelligence System - Demo Script

This script demonstrates the power of CrewAI multi-agent systems for product analysis.
Perfect for LinkedIn showcases and technical demonstrations.

Author: Your Name
Date: July 2025
"""

import pandas as pd
import os
from crewai_main import CrewAIProductAnalyzer, setup_crewai_for_your_data

def main():
    """Main demo script"""
    
    print("🎯" + "=" * 70 + "🎯")
    print("🎁 CREWAI PRODUCT INTELLIGENCE SYSTEM - LIVE DEMO 🎁")
    print("🎯" + "=" * 70 + "🎯")
    print()
    print("👨‍💼 Welcome to the future of product analytics!")
    print("🤖 Watch as 4 AI agents work together to analyze your products")
    print("📊 Each agent has specialized expertise and tools")
    print()
    
    # Check if your data file exists
    data_file = "trendtagger_sample_data (1).xlsx"  # Your Excel file
    csv_file = "your_data.csv"
    
    if os.path.exists(data_file):
        print(f"📁 Found your data file: {data_file}")
        # Convert Excel to CSV for CrewAI
        df = pd.read_excel(data_file)
        df.to_csv(csv_file, index=False)
        print(f"✅ Converted to CSV: {csv_file}")
    else:
        print(f"❌ Data file not found: {data_file}")
        print("🔧 Creating sample data for demo...")
        create_sample_data(csv_file)
    
    print()
    print("🚀 INITIALIZING CREWAI SYSTEM...")
    
    # Setup CrewAI analyzer
    analyzer, products = setup_crewai_for_your_data(csv_file)
    
    if analyzer is None:
        print("❌ Failed to initialize CrewAI system")
        return
    
    print()
    print("🎯 SELECT ANALYSIS MODE:")
    print("1️⃣  Analyze single product (quick demo)")
    print("2️⃣  Analyze all products (full showcase)")
    print("3️⃣  Show CrewAI system details")
    
    choice = input("\n👆 Enter your choice (1-3): ").strip()
    
    if choice == "1":
        # Single product analysis
        print(f"\n🎯 SINGLE PRODUCT ANALYSIS MODE")
        print(f"📦 Available products: {products}")
        
        if products:
            selected_product = products[0]  # Use first product
            print(f"🎯 Analyzing: {selected_product}")
            print()
            
            result = analyzer.analyze_product(selected_product, verbose=True)
            
            print("\n📋 ANALYSIS COMPLETE!")
            print("💾 Results stored in analyzer.results")
            
    elif choice == "2":
        # All products analysis
        print(f"\n🎯 FULL PORTFOLIO ANALYSIS MODE")
        print(f"📦 Will analyze all {len(products)} products")
        
        confirm = input("⚠️  This will take several minutes. Continue? (y/n): ").strip().lower()
        
        if confirm == 'y':
            results = analyzer.analyze_multiple_products(products, verbose=True)
            
            print("\n🎉 FULL ANALYSIS COMPLETE!")
            print(f"📊 Analyzed {len(results)} products")
            print("💾 All results stored in analyzer.results")
            
            # Show summary
            print("\n📊 QUICK SUMMARY:")
            for product, result in results.items():
                print(f"   📦 {product}: Analysis completed")
        else:
            print("❌ Analysis cancelled")
            
    elif choice == "3":
        # Show system details
        print("\n🤖 CREWAI SYSTEM ARCHITECTURE:")
        summary = analyzer.get_crew_summary()
        
        print(f"\n🏢 System: {summary['system_name']}")
        print(f"⚙️  Process: {summary['process_type']}")
        print(f"🤖 Total Agents: {len(summary['agents'])}")
        
        print("\n👥 AI AGENT TEAM:")
        for i, agent in enumerate(summary['agents'], 1):
            print(f"\n   {i}. {agent['name']}")
            print(f"      🎯 Role: {agent['role']}")
            print(f"      🛠️  Tools: {', '.join(agent['tools'])}")
        
        print("\n🎯 SYSTEM CAPABILITIES:")
        for capability in summary['capabilities']:
            print(f"   ✅ {capability}")
    
    else:
        print("❌ Invalid choice")
    
    print("\n" + "🎯" + "=" * 70 + "🎯")
    print("🎁 CREWAI DEMO SESSION COMPLETE! 🎁")
    print("📸 Perfect for LinkedIn screenshots and technical showcases!")
    print("🎯" + "=" * 70 + "🎯")

def create_sample_data(csv_file):
    """Create sample data if real data not available"""
    
    import numpy as np
    from datetime import datetime, timedelta
    
    # Create sample data similar to your format
    dates = pd.date_range('2022-01-01', periods=104, freq='W')  # 2 years weekly
    products = ['GlowCandle_X', 'ClassicMug_Y', 'RoseBox_Z']
    
    data = []
    for product in products:
        for i, date in enumerate(dates):
            # Different patterns for each product
            if product == 'GlowCandle_X':
                # Rising trend
                base_sales = 20 + (i * 0.5) + np.random.normal(0, 5)
            elif product == 'ClassicMug_Y':
                # Stable with slight seasonality
                base_sales = 50 + np.sin(i/8) * 10 + np.random.normal(0, 8)
            else:  # RoseBox_Z
                # Seasonal pattern
                base_sales = 30 + np.sin(i/26) * 20 + np.random.normal(0, 10)
            
            data.append({
                'Product': product,
                'Date': date.strftime('%Y-%m-%d'),
                'Units_Sold': max(1, int(base_sales))
            })
    
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f"✅ Sample data created: {csv_file}")

if __name__ == "__main__":
    main()