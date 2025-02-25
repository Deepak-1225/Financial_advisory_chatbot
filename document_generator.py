import os
from fpdf import FPDF

def create_comprehensive_financial_documents():
    """Create a diverse set of financial documents for testing"""
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # 1. Investment Strategies Document
    investment_pdf = FPDF()
    investment_pdf.add_page()
    investment_pdf.set_font("Arial", size=12)
    
    investment_content = [
        "Investment Strategies for Modern Portfolios",
        "\nDiversification Principles",
        "A well-diversified portfolio requires strategic allocation across multiple asset classes. Modern portfolio theory suggests including a mix of stocks (40-60%), bonds (20-40%), and alternative investments (10-20%). Geographic diversification across developed and emerging markets provides further risk reduction benefits.",
        "\nRisk Management Framework",
        "Effective risk management involves regular portfolio rebalancing, position sizing, and monitoring market conditions. Setting clear stop-loss levels and implementing hedging strategies during volatile market periods helps preserve capital while allowing for optimal growth opportunities.",
        "\nLong-term Investment Approach",
        "Successful investors focus on long-term wealth creation rather than short-term market fluctuations. This approach involves dollar-cost averaging, dividend reinvestment, and tax-efficient investment strategies that compound returns over extended periods."
    ]
    
    for content in investment_content:
        investment_pdf.multi_cell(0, 10, txt=content)
        
    investment_pdf.output("data/investment_strategies.pdf")
    
    # 2. Retirement Planning Guide
    retirement_pdf = FPDF()
    retirement_pdf.add_page()
    retirement_pdf.set_font("Arial", size=12)
    
    retirement_content = [
        "Comprehensive Retirement Planning Guide",
        "\nRetirement Income Strategies",
        "A successful retirement plan should aim to replace 70-80% of pre-retirement income. This typically comes from multiple sources: Social Security benefits, employer-sponsored retirement plans (401(k), 403(b), pension), and personal savings including IRAs and taxable investment accounts.",
        "\nTax-Efficient Withdrawal Strategies",
        "Strategic withdrawals from retirement accounts can significantly impact tax liability. Generally, it's advisable to withdraw from taxable accounts first, then tax-deferred accounts like traditional IRAs and 401(k)s, and finally tax-free accounts like Roth IRAs. This strategy often maximizes after-tax retirement income.",
        "\nLong-term Care Planning",
        "Approximately 70% of retirees will require some form of long-term care. Options for funding include long-term care insurance, health savings accounts (HSAs), self-funding through investments, and Medicaid planning. The ideal strategy depends on individual health factors and financial resources."
    ]
    
    for content in retirement_content:
        retirement_pdf.multi_cell(0, 10, txt=content)
        
    retirement_pdf.output("data/retirement_planning.pdf")
    
    # 3. Tax Optimization Strategies
    tax_pdf = FPDF()
    tax_pdf.add_page()
    tax_pdf.set_font("Arial", size=12)
    
    tax_content = [
        "Tax Optimization Strategies for Investors",
        "\nTax-Loss Harvesting",
        "Tax-loss harvesting involves selling investments that have experienced losses to offset capital gains tax liability. This strategy can reduce taxable income by up to $3,000 per year, with additional losses carried forward to future tax years. It's particularly effective when rebalancing portfolios in tax-inefficient accounts.",
        "\nTax-Advantaged Accounts",
        "Maximizing contributions to tax-advantaged accounts like 401(k)s, IRAs, and HSAs can significantly reduce current and future tax liability. For 2023, contribution limits are $22,500 for 401(k)s, $6,500 for IRAs, and $3,850 for individual HSAs. Catch-up contributions are available for those over 50.",
        "\nAsset Location Strategy",
        "Strategic placement of investments across taxable and tax-advantaged accounts can enhance after-tax returns. Generally, tax-inefficient investments (bonds, REITs) should be held in tax-advantaged accounts, while tax-efficient investments (index funds, growth stocks) are better suited for taxable accounts."
    ]
    
    for content in tax_content:
        tax_pdf.multi_cell(0, 10, txt=content)
        
    tax_pdf.output("data/tax_optimization.pdf")
    
    # 4. Market Analysis and Economic Outlook
    market_pdf = FPDF()
    market_pdf.add_page()
    market_pdf.set_font("Arial", size=12)
    
    market_content = [
        "Current Market Analysis and Economic Outlook",
        "\nEconomic Indicators and Market Performance",
        "Key economic indicators including GDP growth, inflation rates, unemployment figures, and central bank policies provide essential context for investment decisions. These macroeconomic factors influence sector performance and should inform strategic asset allocation decisions.",
        "\nSector Rotation Strategies",
        "Different market sectors perform optimally at various points in the economic cycle. During economic expansion, cyclical sectors like technology and consumer discretionary typically outperform. In contrast, defensive sectors like utilities and consumer staples often excel during economic contractions.",
        "\nValuation Metrics",
        "Fundamental analysis relies on valuation metrics such as P/E ratios, price-to-book ratios, and dividend yields to identify potential investment opp