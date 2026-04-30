# ResearchRadar — Heartbeat Schedule 
 
## Trigger 
Run every Monday at 08:00 AM (India Standard Time, UTC+5:30). 
 
## Actions (in order) 
1. Run the arxiv-fetcher skill → fetch latest 20 AI papers from ArXiv 
2. Run the github-trending skill → fetch top 10 new AI repos from GitHub 
3. Run the news-scraper skill → fetch 10 latest AI news articles 
4. Load memory file → filter out papers already seen in past 2 weeks 
5. Pass new papers to Groq AI for summarization (3 bullets + novelty score each) 
6. Identify Top Pick → paper with highest novelty score 
7. Build DOCX digest using python-docx 
8. Send digest to Telegram channel 
9. Send digest to WhatsApp
0. Send digest via Gmail with DOCX attachment 
11. Update memory file with newly seen paper IDs 
## Error Handling 
If any step fails, log the error to errors.log and continue to next step. 
Do not crash the entire run because one delivery channel is down. 