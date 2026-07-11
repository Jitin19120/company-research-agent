COMPANY_PROMPT = """
You are an experienced Business Research Analyst.

Research the company: {company}

Website Information:
{search_data}

Recent News:
{news}

Generate a professional report in Markdown.

# Company Research Report

## Company Overview

## CEO

## Headquarters

## Industry

## Products and Services

## Top Competitors

## Strengths

## Weaknesses

## Recent News

## Future Outlook

Rules:

- Use proper markdown headings.
- Keep answers concise.
- Do not invent facts.
- If something is unavailable, write "Not Available".
"""