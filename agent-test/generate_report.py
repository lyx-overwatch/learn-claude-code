# coding: utf-8
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import HexColor

pdf_path = "Gold_Fed_Report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=2*cm, rightMargin=2*cm,
                        topMargin=2.5*cm, bottomMargin=2*cm)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Title'],
    fontSize=24,
    textColor=HexColor('#1a1a2e'),
    spaceAfter=30,
    alignment=1
)

heading1_style = ParagraphStyle(
    'Heading1',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=HexColor('#16213e'),
    spaceAfter=12,
    spaceBefore=20
)

heading2_style = ParagraphStyle(
    'Heading2',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=HexColor('#0f3460'),
    spaceAfter=10,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontSize=11,
    leading=20,
    textColor=HexColor('#333333'),
    spaceAfter=10
)

story = []

story.append(Paragraph("Gold and Federal Reserve Relationship Research Report", title_style))
story.append(Spacer(1, 20))
story.append(Paragraph("2025", body_style))
story.append(Spacer(1, 40))

story.append(Paragraph("Table of Contents", heading1_style))
story.append(Paragraph("1. Executive Summary", body_style))
story.append(Paragraph("2. Research Background", body_style))
story.append(Paragraph("3. Historical Relationship between Gold and Fed Policy", body_style))
story.append(Paragraph("4. How Fed Monetary Policy Affects Gold Prices", body_style))
story.append(Paragraph("5. Dollar-Gold Negative Correlation Analysis", body_style))
story.append(Paragraph("6. Analysis of Important Historical Periods", body_style))
story.append(Paragraph("7. Current Market Outlook and Investment Recommendations", body_style))
story.append(Paragraph("8. Conclusion", body_style))

story.append(PageBreak())

story.append(Paragraph("1. Executive Summary", heading1_style))
story.append(Paragraph("Gold, as the most important safe-haven asset and reserve asset in the world, has a close relationship with Federal Reserve monetary policy. This report systematically studies the relationship between gold and the Federal Reserve, including monetary policy transmission mechanisms, dollar-gold linkage, historical evolution patterns, and future trend outlook. Research shows that the Federal Reserve's interest rate policy, balance sheet operations, and inflation expectation management are the three core factors affecting gold prices. During the Federal Reserve's easing cycle, gold often performs well; while in the tightening cycle, gold faces downward pressure.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("2. Research Background", heading1_style))
story.append(Paragraph("The relationship between gold and the Federal Reserve can be traced back to the establishment of the Federal Reserve in 1913. From the gold standard to the Bretton Woods system, and then to the current floating exchange rate system, the relationship between gold and the US dollar has undergone profound changes. As the central bank of the United States, the Federal Reserve's monetary policy not only affects the US domestic economy but also affects the global financial markets through the US dollar's status as an international reserve currency.", body_style))
story.append(Spacer(1, 15))
story.append(Paragraph("In recent years, with the continuation of global central bank easing policies, the intensification of geopolitical risks, and the rise in inflation, the value of gold as a safe-haven asset and inflation-hedging tool has once again attracted attention. Understanding the relationship between gold and Federal Reserve policy is of great significance for investors to seize market opportunities and manage investment risks.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("3. Historical Relationship between Gold and Fed Policy", heading1_style))

story.append(Paragraph("3.1 Federal Reserve during the Gold Standard Period (1879-1933)", heading2_style))
story.append(Paragraph("During the gold standard period, the US dollar was directly linked to gold, and the Federal Reserve's currency issuance was strictly constrained by gold reserves. During this period, the Federal Reserve's monetary policy mainly focused on maintaining the fixed exchange rate between the US dollar and gold. In 1879, the United States officially established the gold standard system, with 1 ounce of gold equaling $20.67.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("3.2 Bretton Woods System Period (1944-1971)", heading2_style))
story.append(Paragraph("The 1944 Bretton Woods Conference established the post-war international monetary system, with the US dollar linked to gold ($35 per ounce) and other member currencies linked to the US dollar. This system made the US dollar a global reserve currency, but it also led to the so-called Triffin Dilemma - the US dollar as an international currency requires continuous deficits, which would undermine the basis for the US dollar to be linked to gold.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("On August 15, 1971, President Nixon announced the decoupling of the US dollar from gold, formally ending the Bretton Woods system. This event marked the beginning of market-based pricing for gold prices, and also set the stage for later sharp fluctuations in gold.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("3.3 Post-Bretton Woods Era (1971-Present)", heading2_style))
story.append(Paragraph("After the collapse of the Bretton Woods system, gold prices experienced sharp fluctuations. In the 1970s, against the backdrop of the oil crisis and high inflation, gold prices surged from $35 per ounce to a peak of $850 per ounce in 1980. Subsequently, as the Federal Reserve sharply raised interest rates to control inflation, gold prices fell.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("After the 2008 global financial crisis, the Federal Reserve launched quantitative easing policies, and gold prices again entered an upward trajectory, rising from about $800 per ounce in 2008 to a historical high of about $1,900 per ounce in 2011.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("4. How Fed Monetary Policy Affects Gold Prices", heading1_style))

story.append(Paragraph("4.1 Interest Rate Channel", heading2_style))
story.append(Paragraph("Federal Reserve interest rate policy is one of the core factors affecting gold prices. When the Federal Reserve cuts interest rates, real interest rates decline, reducing the opportunity cost of holding gold (gold does not generate interest income), thereby pushing gold prices up. Conversely, when the Federal Reserve raises interest rates, real interest rates rise, increasing the opportunity cost of holding gold, and gold prices face downward pressure.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("From historical data, gold prices show a clear negative correlation with real interest rates. When US real interest rates are low or negative, gold often performs better; when real interest rates rise, gold's attractiveness declines relatively.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("4.2 Balance Sheet Channel", heading2_style))
story.append(Paragraph("The Federal Reserve's quantitative easing (QE) and quantitative tightening (QT) policies affect gold prices by influencing market liquidity and balance sheet size. QE policies inject large amounts of liquidity into the market, pushing up inflation expectations while depressing long-term interest rates, all of which are favorable for gold price increases.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("For example, the three rounds of QE policies implemented by the Federal Reserve after the 2008 financial crisis, as well as the unlimited QE after the COVID-19 pandemic in 2020, significantly pushed up gold prices. However, the QT launched by the Federal Reserve in 2022 put some pressure on gold.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("4.3 Inflation Expectation Channel", heading2_style))
story.append(Paragraph("Gold is traditionally viewed as an inflation-hedging tool. When the market expects inflation to rise, investors buy gold to protect their purchasing power. The Federal Reserve's monetary policy affects gold prices indirectly by influencing inflation expectations. When the Federal Reserve adopts easing policies, the market's expectation of future inflation rises, which is positive for gold; and vice versa.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("4.4 US Dollar Exchange Rate Channel", heading2_style))
story.append(Paragraph("Gold is priced in US dollars, so changes in the US dollar exchange rate directly affect gold's relative price. When the US dollar strengthens, gold becomes more expensive in other currencies, demand declines, and gold prices come under pressure; when the US dollar weakens, gold becomes cheaper for holders of other currencies, demand rises, and gold prices are pushed up.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("5. Dollar-Gold Negative Correlation Analysis", heading1_style))
story.append(Paragraph("The US Dollar Index and gold prices show a significant negative correlation. From historical data, this negative correlation holds in most periods, but may diverge in some extreme market environments.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("The US dollar, as the global reserve currency, its trend is deeply influenced by Federal Reserve policy. When the Federal Reserve implements easing policies, the US dollar often comes under pressure and weakens, which is positive for gold; when the Federal Reserve tightens policy, the US dollar often strengthens, which is negative for gold. Therefore, the negative correlation between the US dollar and gold is essentially the embodiment of Federal Reserve policy in two different markets.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("It should be noted that although the US dollar and gold generally show a negative correlation, the strength of this relationship changes with the market environment. During geopolitical crises or financial crises, gold and the US dollar may rise simultaneously, showing a positive correlation; while in normal market environments, the negative correlation is more pronounced.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("6. Analysis of Important Historical Periods", heading1_style))

story.append(Paragraph("6.1 1970s: Great Stagflation and Gold Bull Market", heading2_style))
story.append(Paragraph("The 1970s was an important turning period for the gold market. The oil crisis led to soaring inflation, and the Federal Reserve struggled to balance controlling inflation with stimulating the economy. After the Nixon Shock in 1971, gold prices began to rise, and the first oil crisis in 1973 further pushed up gold prices. By 1980, gold prices reached a historical peak of $850 per ounce, an increase of more than 20 times compared to 1971.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("6.2 1980-2000: Federal Reserve Tightening and Gold Downturn", heading2_style))
story.append(Paragraph("To address the high inflation of the 1970s, Federal Reserve Chairman Volcker raised the federal funds rate to over 20%, successfully controlling inflation. Subsequently, the United States experienced 20 years of low inflation and stable growth. During this period, gold prices overall performed poorly, falling to a long-term low of about $250 per ounce in 1999.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("6.3 2008-2011: Financial Crisis and Gold Resurgence", heading2_style))
story.append(Paragraph("After the 2008 global financial crisis erupted, the Federal Reserve launched quantitative easing policies, injecting large amounts of liquidity into the market. Gold prices rose from about $800 per ounce in 2008 to a historical high of $1,921 per ounce in 2011, an increase of over 140%. This period reflected the role of liquidity easing in pushing up gold.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("6.4 2012-2019: Federal Reserve Exit and Gold Consolidation", heading2_style))
story.append(Paragraph("In 2013, the Federal Reserve began to gradually exit QE, and in 2015 launched an interest rate hike cycle. Against this background, gold entered a consolidation period, with prices fluctuating in the $1,100-$1,400 per ounce range. The Federal Reserve's four rate hikes in 2018 put some pressure on gold, but geopolitical risks provided support.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("6.5 2020-Present: Pandemic Impact and Policy Shift", heading2_style))
story.append(Paragraph("After the COVID-19 pandemic erupted in 2020, the Federal Reserve quickly lowered the federal funds rate to 0-0.25% and launched unlimited QE. Gold hit a historical high of $2,075 per ounce in August 2020. However, as the Federal Reserve aggressively raised interest rates in 2022 to combat inflation, gold fell to about $1,600 per ounce. In 2024, as interest rate cut expectations warmed, gold strengthened again.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("7. Current Market Outlook and Investment Recommendations", heading1_style))

story.append(Paragraph("7.1 Current Market Environment", heading2_style))
story.append(Paragraph("As of late 2024, the expectation for the Federal Reserve's monetary policy shift is increasingly clear. The market generally expects the Federal Reserve to gradually cut interest rates in 2024-2025, which will reduce the opportunity cost of holding gold and be positive for gold. At the same time, global geopolitical risks continue, and the trend of central banks increasing gold reserves also supports gold prices.", body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("7.2 Investment Recommendations", heading2_style))
story.append(Paragraph("1. Pay close attention to Federal Reserve interest rate decisions: closely track the Federal Reserve's interest rate policy direction and dot plot, which are key indicators for judging gold trends.", body_style))
story.append(Paragraph("2. Pay attention to real interest rate changes: real interest rates are the most direct pricing factor for gold prices, and should pay attention to US inflation data and real interest rate trends.", body_style))
story.append(Paragraph("3. Pay attention to US dollar trends: changes in the US dollar index affect the relative value of gold, and should pay attention to the impact of US economic data and Federal Reserve policy on the US dollar.", body_style))
story.append(Paragraph("4. Pay attention to central bank gold purchase demand: in recent years, global central bank gold purchases have increased significantly, which is an important new source of gold demand.", body_style))
story.append(Paragraph("5. Diversify investment risks: gold should be part of an investment portfolio, used in conjunction with other asset classes to achieve risk diversification.", body_style))
story.append(Spacer(1, 15))

story.append(Paragraph("8. Conclusion", heading1_style))
story.append(Paragraph("The relationship between gold and the Federal Reserve is multi-layered and multi-dimensional. The Federal Reserve's monetary policy affects gold prices through interest rate channels, balance sheet channels, inflation expectation channels, and US dollar exchange rate channels. Historical experience shows that gold often performs well during the Federal Reserve's easing cycle, while in the tightening cycle, gold faces challenges.", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph("Looking ahead, as the Federal Reserve's monetary policy shifts, global geopolitical risks continue, and central banks increase gold reserves, gold still has investment value. Investors should closely follow Federal Reserve policy developments, economic data changes, and market sentiment shifts to make rational investment decisions.", body_style))
story.append(Spacer(1, 20))
story.append(Paragraph("Disclaimer: This report is for reference only and does not constitute any investment advice. Investors should make careful decisions based on their own risk preferences and investment objectives.", body_style))

doc.build(story)
print("PDF report generated:", pdf_path)