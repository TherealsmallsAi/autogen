# Small Talk AI News Landing Page Generator

This tool automates creating cyber-style AI news landing pages from a JSON payload.

## Quick start

```bash
python tools/small-talk-news/generate_landing_page.py
```

Generate from a custom story payload:

```bash
python tools/small-talk-news/generate_landing_page.py \
  --story-json tools/small-talk-news/story.example.json
```

The script writes each page to `tools/small-talk-news/output/` using a timestamped filename.

## JSON shape

Use `tools/small-talk-news/story.example.json` as the base schema. You can swap headlines, cards, hashtags, and log lines for each new post.

## Run all day every day

Example cron entry (hourly):

```bash
0 * * * * cd /workspace/autogen && /usr/bin/python3 tools/small-talk-news/generate_landing_page.py --story-json /path/to/latest_story.json
```

To publish continuously, pair this with your own upstream story generation pipeline and deployment job to GitHub Pages/Netlify/Vercel.
