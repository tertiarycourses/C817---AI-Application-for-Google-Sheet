"""
Domain 2 — Analysing and Automating Data with AI in Sheets. Labs 5-8.

Continues the SAME Riverside Supplies dataset from Domain 1. Having generated and
explained formulas, you now use AI to clean and organise the data, summarise and
analyse it, turn it into tables and charts, and finally validate AI output and set
your own rules for applying AI safely to real work data. Lab 8 is the capstone.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside "
 "Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs."
)

DOMAIN2 = [
 dict(
 num=5, topic=2,
 title="Clean, Transform and Organise Data with AI",
 objective="Use AI to standardise messy text and dates, tidy fields, and organise the dataset into a clean table.",
 desc="Analysis is only as good as the data under it. You use Gemini to standardise the messy Region and "
 "Product text, fix the mixed date formats, and sort the records into a clean, consistent table — asking "
 "AI for the formula or steps each time and verifying the result. " + PROJECT_NOTE,
 build="A cleaned, consistently formatted Orders table ready for analysis.",
 services="Gemini side panel, TRIM, PROPER, CLEAN, date formatting, Data > Sort range",
 steps=[
 ("Ask AI how to standardise the Region column so 'north', 'North ' and 'NORTH' all become 'North'.",
  "Give me a formula for column J that returns column D with consistent capitalisation and no leading or trailing spaces."),
 ("Put the formula in J2 and fill it down; check that a few previously messy rows now read cleanly.",
  "=PROPER(TRIM(D2))"),
 ("Lock the fix in: copy column J, then Edit > Paste special > Values only over column D, and delete the helper column J.", ""),
 ("Ask AI to standardise the Order Date column to YYYY-MM-DD, and follow its steps (Format > Number > Date, or the formula it gives).",
  "Column B has dates in mixed formats. How do I make them all display as YYYY-MM-DD in Google Sheets?"),
 ("Verify a couple of dates against what they clearly should be, and confirm none turned blank or wrong.", ""),
 ("Tidy the Product column: ask AI for a formula to trim extra spaces and fix capitalisation, apply it, and paste values back as in step 3.",
  "=TRIM(E2)"),
 ("Organise the data: select A1:I200 and use Data > Sort range (with 'Data has header row' ticked) to sort by Order Date, ascending.", ""),
 ("Ask Gemini to check your work.",
  "Look at the Orders tab. Are there any remaining blank cells, inconsistent categories or duplicate Order IDs I should fix?"),
 ],
 test="The Region and Product columns are consistent, all Order Dates display as YYYY-MM-DD, the data is sorted by date, and Gemini's check reports no remaining obvious issues (or you have fixed the ones it named).",
 ),
 dict(
 num=6, topic=2,
 title="Summarise and Analyse Your Dataset with AI",
 objective="Use AI to summarise the dataset and answer analytical questions, verifying every figure against a formula.",
 desc="With clean data you can ask real questions. You have Gemini summarise the quarter, compare segments "
 "and describe the trend across the three months — and you verify every figure it gives against a formula "
 "or count you compute yourself before you trust it. " + PROJECT_NOTE,
 build="A short, written analysis of the quarter in which every figure has been verified.",
 services="Gemini side panel, summarisation, AVERAGE, SUMIFS, segment analysis",
 steps=[
 ("Ask AI for a summary of the quarter.",
  "Summarise the Orders tab: total sales value, number of orders, average order value, and the best-selling product. Show the figure for each."),
 ("Verify the total sales against your grand total from Lab 2 (cell K1) — they should match.", ""),
 ("Verify the average order value yourself.",
  "=AVERAGE(I2:I200)"),
 ("Ask a segment question.",
  "Which Region had the highest total sales, and by how much more than the second-highest?"),
 ("Cross-check the winning region with a SUMIF like the one you built in Lab 3.", ""),
 ("Ask an analytical trend question.",
  "Did sales grow or fall across the three months in this quarter? Give the monthly total for each month and describe the trend in one sentence."),
 ("Verify the monthly totals with a quick pivot or a SUMIFS by month; if any figure does not match, investigate before trusting it.", ""),
 ("Write a 3-bullet summary of the quarter in a notes area, using only figures you have verified.", ""),
 ],
 test="You have a written 3-bullet summary in which every figure — total sales, average order value and the top region — matches a formula or count you computed yourself.",
 ),
 dict(
 num=7, topic=2,
 title="Create Tables, Charts and Visualisations with AI",
 objective="Use AI to build a summary/pivot table and the right, clearly labelled chart to tell the data's story.",
 desc="Numbers persuade when they are shown well. You use Gemini to design a pivot of sales by region and "
 "month, then to recommend and build the right chart, and to refine its title, labels and sorting — "
 "checking each visual against the figures you verified in Lab 6. " + PROJECT_NOTE,
 build="A verified pivot table plus a labelled column chart and a monthly-trend line chart.",
 services="Gemini side panel, pivot tables, Insert > Chart, chart types, chart formatting",
 steps=[
 ("Ask AI which summary table best shows sales performance and how to build it.",
  "I want to see total sales by Region and by month. What pivot table should I build, and what are the steps in Google Sheets?"),
 ("Build the pivot (Insert > Pivot table): Rows = Region, Columns = month of Order Date, Values = SUM of Total.", ""),
 ("Verify one cell of the pivot against a SUMIFS you write for that same region and month.", ""),
 ("Ask AI to recommend the best chart to compare sales across regions.",
  "What is the best chart type to compare total sales across Regions, and why?"),
 ("Insert the chart: select the region totals, then Insert > Chart, and set the recommended type (for example a column chart).", ""),
 ("Ask AI to improve it, then apply the suggestions — a clear title, axis labels, and bars sorted highest to lowest.",
  "Suggest a clear title and axis labels for a column chart of total sales by Region, sorted highest to lowest."),
 ("Add a second chart for the monthly trend: a line chart of total sales by month.", ""),
 ("Check the trend chart matches the direction you found in your Lab 6 analysis.", ""),
 ],
 test="You have a pivot table whose figures you verified against a formula, a labelled column chart of sales by region sorted high-to-low, and a line chart of the monthly trend consistent with your Lab 6 analysis.",
 ),
 dict(
 num=8, topic=2,
 title="Validate AI Output and Apply AI Safely to Work Data",
 objective="Stress-test AI output for accuracy and write a personal checklist for applying AI safely to real work data.",
 desc="The capstone. You deliberately test whether AI's answers hold up, learn to verify anything before you "
 "act on it, review what data is safe to put into a prompt, and write a safe-use checklist you apply to an "
 "earlier result — the habits that make AI in Sheets trustworthy at work. " + PROJECT_NOTE,
 build="A verification habit and a written safe-use checklist you have applied to an earlier lab's result.",
 services="Validation, cross-checking, data privacy, safe-use checklist",
 steps=[
 ("Ask AI a question with a knowable answer, then verify it with a formula.",
  "How many orders are from the North region?"),
 ("Confirm the count yourself and compare.",
  "=COUNTIF(D2:D200,\"North\")"),
 ("Try to catch a mistake: ask a trickier question and verify hard by recomputing it yourself.",
  "What percentage of total sales came from the top 3 customers? Show the range you used and the working."),
 ("If the AI figure is wrong or unclear, refine the prompt (state the range and ask it to show its working) and re-run.", ""),
 ("Set the rule: never accept an AI number you cannot tie back to a formula or count in the sheet.", ""),
 ("Review data safety: list which columns here would be sensitive if this were real company data (for example Customer names), and how you would protect them.", ""),
 ("Ask AI for good practice, then sanity-check its advice against your own judgement.",
  "What should I avoid putting into an AI prompt when working with real company data, and why?"),
 ("Draft your safe-use checklist — verify every figure; keep confidential data out of prompts; state the range; ask for the formula; record where AI was used — and apply it to one AI result from an earlier lab.", ""),
 ],
 test="You have caught or ruled out at least one AI inaccuracy by verifying it against your own formula, and you have a written safe-use checklist that you applied to an earlier lab's result.",
 ),
]
