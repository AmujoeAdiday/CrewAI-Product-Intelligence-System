from crewai import Task

def create_seasonality_task(agent, data_path: str, product_name: str):
    """Create a seasonality analysis task for a specific product"""
    return Task(
        description=f"""
        🌊 SEASONALITY ANALYSIS MISSION for {product_name}
        
        As the Senior Seasonality Analyst, your mission is to uncover the hidden seasonal patterns 
        in {product_name}'s sales data. This analysis will directly impact inventory planning and 
        marketing campaign timing.
        
        SPECIFIC OBJECTIVES:
        1. 📊 Calculate precise seasonality metrics and strength scores
        2. 🎯 Identify the top 3 peak months and bottom 3 low months
        3. 🔍 Determine if this product exhibits true seasonal behavior
        4. 💡 Provide strategic insights for inventory and marketing planning
        5. ⚠️ Flag any unusual seasonal anomalies that need attention
        
        DATA SOURCE: {data_path}
        TARGET PRODUCT: {product_name}
        
        DELIVERABLE: A comprehensive seasonality report with actionable recommendations
        for business strategy and operational planning.
        """,
        agent=agent,
        expected_output="""A detailed seasonality analysis report containing:
        - Seasonality strength score and interpretation
        - Peak and low season identification with specific months
        - Clear YES/NO determination on seasonal behavior
        - Monthly performance averages and insights
        - Strategic recommendations for inventory planning
        - Marketing timing suggestions based on seasonal patterns
        - Risk assessment for seasonal dependency""",
        tools=[agent.tools[0]] if agent.tools else []
    )

def create_trend_task(agent, data_path: str, product_name: str):
    """Create a trend analysis task for a specific product"""
    return Task(
        description=f"""
        📈 TREND ANALYSIS MISSION for {product_name}
        
        As the Senior Business Trend Analyst, your mission is to decode the long-term trajectory 
        of {product_name} and predict its future performance. Your analysis will influence major 
        investment and strategic decisions.
        
        SPECIFIC OBJECTIVES:
        1. 📊 Calculate precise trend slopes and statistical confidence levels
        2. 🎯 Analyze both overall and recent (12-week) performance trends
        3. 📈 Determine trend direction (rising, declining, or stable)
        4. 💪 Assess trend strength and reliability for forecasting
        5. 📊 Calculate total growth/decline percentages over the analysis period
        6. 🔮 Provide forward-looking insights and confidence levels
        
        DATA SOURCE: {data_path}
        TARGET PRODUCT: {product_name}
        
        DELIVERABLE: A comprehensive trend analysis with statistical backing and 
        strategic implications for product portfolio management.
        """,
        agent=agent,
        expected_output="""A detailed trend analysis report containing:
        - Overall trend direction and slope calculation
        - Recent performance trend (last 12 weeks) analysis
        - R-squared values and statistical confidence levels
        - Total percentage change over the analysis period
        - Trend strength classification (Strong/Moderate/Weak)
        - Forward-looking performance predictions
        - Strategic recommendations for investment decisions
        - Risk assessment based on trend reliability""",
        tools=[agent.tools[0]] if agent.tools else []
    )

def create_classification_task(agent, data_path: str, product_name: str):
    """Create a product classification task"""
    return Task(
        description=f"""
        🏷️ PRODUCT CLASSIFICATION MISSION for {product_name}
        
        As the Chief Product Strategy Consultant, your mission is to synthesize all analytical 
        findings and classify {product_name} into a strategic category that will guide executive 
        decision-making and resource allocation.
        
        STRATEGIC CLASSIFICATION FRAMEWORK:
        🔥 RISING STAR - High growth potential, invest heavily
        💘 SEASONAL HERO - Seasonal patterns, optimize timing
        🌲 EVERGREEN - Stable performer, reliable revenue
        💤 FADING OUT - Declining, consider exit strategy
        🎲 RANDOM/ERRATIC - Unpredictable, investigate causes
        📉 DECLINING SEASONAL - Seasonal but losing steam
        📊 STABLE - Steady performance, maintain current strategy
        
        SPECIFIC OBJECTIVES:
        1. 🎯 Assign definitive strategic classification with confidence score
        2. 💡 Provide clear reasoning based on trend and seasonality data
        3. 📋 Generate specific action items for product management
        4. 💰 Estimate investment priority level (High/Medium/Low)
        5. ⚠️ Identify key risks and opportunities
        6. 🎯 Recommend KPIs to monitor going forward
        
        DATA SOURCE: {data_path}
        TARGET PRODUCT: {product_name}
        
        DELIVERABLE: Executive-ready product classification with strategic roadmap.
        """,
        agent=agent,
        expected_output="""A strategic product classification report containing:
        - Primary classification category with confidence percentage
        - Detailed reasoning based on quantitative analysis
        - Specific action items for product management team
        - Investment priority recommendation (High/Medium/Low)
        - Risk assessment and mitigation strategies
        - Opportunity identification and growth potential
        - Recommended KPIs for ongoing monitoring
        - Executive summary suitable for board presentation""",
        tools=[agent.tools[0]] if agent.tools else []
    )

def create_orchestration_task(agent, data_path: str, product_name: str):
    """Create the main orchestration task for the Chief Analyst"""
    return Task(
        description=f"""
        🎯 COMPREHENSIVE PRODUCT INTELLIGENCE MISSION for {product_name}
        
        As the Chief Data Science Officer, your mission is to orchestrate a complete 
        product intelligence analysis by coordinating your team of specialist agents. 
        This analysis will directly inform C-level strategic decisions.
        
        COORDINATION OBJECTIVES:
        1. 🎯 Direct the Seasonality Analyst to uncover seasonal patterns
        2. 📈 Guide the Trend Analyst to identify growth/decline trajectories  
        3. 🏷️ Have the Product Strategist synthesize findings into classifications
        4. 📊 Ensure all analyses are aligned and comprehensive
        5. 📋 Compile executive-ready recommendations
        6. ⚠️ Flag any conflicting findings that need resolution
        
        TEAM COORDINATION:
        - Seasonality Analyst: Seasonal pattern identification
        - Trend Analyst: Growth trajectory analysis
        - Product Strategist: Strategic classification and recommendations
        
        DATA SOURCE: {data_path}
        TARGET PRODUCT: {product_name}
        
        DELIVERABLE: A unified, executive-ready product intelligence report that 
        synthesizes all specialist findings into clear strategic guidance.
        """,
        agent=agent,
        expected_output="""A comprehensive executive product intelligence report containing:
        - Executive summary with key findings and recommendations
        - Synthesis of seasonality, trend, and classification analyses
        - Strategic product category and confidence assessment
        - Prioritized action items with timelines
        - Investment recommendations and resource allocation guidance
        - Risk assessment and mitigation strategies
        - Performance monitoring framework
        - Clear next steps for product management team
        - Board-ready presentation summary""",
        context=[],  # Will be populated with other task results
        tools=[]
    )