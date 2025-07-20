from crewai import Crew, Process
from crewai_agents import (
    seasonality_analyst, 
    trend_analyst, 
    product_strategist,
    chief_analyst
)
from crewai_tasks import (
    create_seasonality_task,
    create_trend_task,
    create_classification_task,
    create_orchestration_task
)
import pandas as pd
from datetime import datetime

class CrewAIProductAnalyzer:
    """
    CrewAI-powered Product Intelligence System
    
    This system uses multiple AI agents working together to analyze product performance:
    - Seasonality Analyst: Identifies seasonal patterns
    - Trend Analyst: Analyzes growth/decline trends  
    - Product Strategist: Classifies products strategically
    - Chief Analyst: Orchestrates the entire analysis
    """
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.results = {}
    
    def analyze_product(self, product_name: str, verbose: bool = True):
        """
        Analyze a single product using the CrewAI multi-agent system
        
        Args:
            product_name (str): Name of the product to analyze
            verbose (bool): Whether to show detailed agent interactions
            
        Returns:
            dict: Complete analysis results from all agents
        """
        
        if verbose:
            print(f"\n🚀 INITIATING CREWAI ANALYSIS FOR: {product_name}")
            print("=" * 60)
            print("🤖 Assembling AI Agent Team...")
            print("   👤 Seasonality Analyst - Ready")
            print("   👤 Trend Analyst - Ready") 
            print("   👤 Product Strategist - Ready")
            print("   👤 Chief Analyst - Ready")
            print("=" * 60)
        
        # Create tasks for each agent
        seasonality_task = create_seasonality_task(
            agent=seasonality_analyst,
            data_path=self.data_path,
            product_name=product_name
        )
        
        trend_task = create_trend_task(
            agent=trend_analyst,
            data_path=self.data_path,
            product_name=product_name
        )
        
        classification_task = create_classification_task(
            agent=product_strategist,
            data_path=self.data_path,
            product_name=product_name
        )
        
        orchestration_task = create_orchestration_task(
            agent=chief_analyst,
            data_path=self.data_path,
            product_name=product_name
        )
        
        # Set up task dependencies
        orchestration_task.context = [seasonality_task, trend_task, classification_task]
        
        # Create the crew
        crew = Crew(
            agents=[
                seasonality_analyst,
                trend_analyst, 
                product_strategist,
                chief_analyst
            ],
            tasks=[
                seasonality_task,
                trend_task,
                classification_task,
                orchestration_task
            ],
            process=Process.sequential,
            verbose=verbose,
            memory=True,
            cache=True
        )
        
        if verbose:
            print(f"🎯 EXECUTING MULTI-AGENT ANALYSIS...")
            print("   🌊 Phase 1: Seasonality Analysis...")
            print("   📈 Phase 2: Trend Analysis...")
            print("   🏷️ Phase 3: Strategic Classification...")
            print("   🎯 Phase 4: Executive Synthesis...")
            print("=" * 60)
        
        # Execute the crew
        try:
            result = crew.kickoff()
            
            # Store results
            self.results[product_name] = {
                'timestamp': datetime.now().isoformat(),
                'analysis_result': result,
                'crew_info': {
                    'agents_used': len(crew.agents),
                    'tasks_completed': len(crew.tasks),
                    'process_type': 'Sequential Multi-Agent'
                }
            }
            
            if verbose:
                print("✅ ANALYSIS COMPLETE!")
                print("=" * 60)
                print(f"📊 RESULTS FOR {product_name}:")
                print("=" * 60)
                print(result)
                print("=" * 60)
            
            return result
            
        except Exception as e:
            error_msg = f"❌ CrewAI Analysis failed for {product_name}: {str(e)}"
            if verbose:
                print(error_msg)
            return error_msg
    
    def analyze_multiple_products(self, product_list: list, verbose: bool = True):
        """
        Analyze multiple products using the CrewAI system
        
        Args:
            product_list (list): List of product names to analyze
            verbose (bool): Whether to show detailed output
            
        Returns:
            dict: Analysis results for all products
        """
        
        if verbose:
            print(f"\n🎯 MULTI-PRODUCT CREWAI ANALYSIS INITIATED")
            print(f"📦 Products to analyze: {len(product_list)}")
            print(f"🤖 AI Agents: 4 (Seasonality, Trend, Strategy, Chief)")
            print("=" * 60)
        
        all_results = {}
        
        for i, product in enumerate(product_list, 1):
            if verbose:
                print(f"\n📊 ANALYZING PRODUCT {i}/{len(product_list)}: {product}")
            
            result = self.analyze_product(product, verbose=verbose)
            all_results[product] = result
            
            if verbose:
                print(f"✅ Completed {product}")
                if i < len(product_list):
                    print("🔄 Moving to next product...\n")
        
        if verbose:
            print(f"\n🎉 ALL ANALYSES COMPLETE!")
            print(f"📊 {len(all_results)} products analyzed successfully")
            print("=" * 60)
        
        return all_results
    
    def get_crew_summary(self):
        """Get a summary of the CrewAI system configuration"""
        return {
            'system_name': 'CrewAI Product Intelligence System',
            'agents': [
                {
                    'name': 'Senior Seasonality Analyst',
                    'role': 'Seasonal pattern identification',
                    'tools': ['SeasonalityAnalysisTool']
                },
                {
                    'name': 'Senior Business Trend Analyst', 
                    'role': 'Growth trend analysis',
                    'tools': ['TrendAnalysisTool']
                },
                {
                    'name': 'Chief Product Strategy Consultant',
                    'role': 'Strategic classification',
                    'tools': ['ProductClassificationTool']
                },
                {
                    'name': 'Chief Data Science Officer',
                    'role': 'Analysis orchestration',
                    'tools': ['Delegation & Coordination']
                }
            ],
            'process_type': 'Sequential Multi-Agent',
            'capabilities': [
                'Seasonal pattern detection',
                'Trend analysis and forecasting',
                'Strategic product classification', 
                'Executive report generation',
                'Multi-agent coordination'
            ]
        }

# Example usage and demo
def demo_crewai_analysis(data_path: str = "sample_data.csv"):
    """
    Demonstration of the CrewAI Product Intelligence System
    """
    
    print("🎁 CREWAI PRODUCT INTELLIGENCE SYSTEM DEMO")
    print("=" * 60)
    
    # Initialize the analyzer
    analyzer =