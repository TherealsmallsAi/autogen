#!/usr/bin/env python3
"""Generate cyber-style AI news landing pages from JSON input."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import re
from typing import Any

DEFAULT_STORY = {
    "page_title": "AI CYBER WARFARE NEWS",
    "brand_name": "SMALL TALK AI NEWS",
    "system_status": "BREACH DETECTED",
    "region": "GLOBAL",
    "threat_level": "CRITICAL",
    "flash_headline": "THE ERA OF SELF-MODIFYING MALWARE",
    "flash_summary": "Google's latest threat report reveals that state-sponsored hacking groups are now using Gemini AI as a component of malware.",
    "primary_headline": "AI CYBER WARFARE IS HERE",
    "primary_body": "The future of hacking just arrived. We aren't just talking about AI-written phishing emails anymore. We're talking about live, AI-generated code executing in memory.",
    "cards": [
        {
            "label": "HONESTCUE MALWARE",
            "color": "pink-600",
            "title_color": "pink-500",
            "body": "This strain calls the Gemini API mid-attack, receives custom C# code, and executes it filelessly in memory.",
        },
        {
            "label": "PROMPTFLUX MALWARE",
            "color": "yellow-500",
            "title_color": "yellow-500",
            "body": "Features a Thinking Robot module that asks Gemini to rewrite malware source code every hour to stay hidden from security tools.",
        },
    ],
    "special_section_title": "PERSONA BUILDING",
    "special_section_body": "APT groups are using AI to build fake cybersecurity personas and trick targets into clicking malicious links.",
    "terminal_log": [
        "Initializing security audit...",
        "Nuking identified malicious accounts...",
        "Hardening Gemini safety filters...",
        "Status: [MITIGATED / WARNING PERSISTS]",
    ],
    "cta_text": "ARE OUR DEFENSES READY FOR CODE THAT REWRITES ITSELF?",
    "hashtags": [
        "CyberSecurity",
        "AI",
        "GoogleGemini",
        "Malware",
        "HackingNews",
        "TechTrends",
    ],
    "copyright_text": "2026 SMALL TALK AI BROADCAST NETWORK | ENCRYPTED TRANSMISSION",
    "console_notice": "Gemini AI Malware Detected in Region 7G",
    "bot_section_title": "SmLs Bot: Always-On Automation Unit",
    "bot_name": "SmLsbot",
    "bot_description": "SmLsbot is a dedicated automation companion for continuous AI news operations, publishing workflows, and monitoring tasks.",
    "bot_repo_url": "https://github.com/therealsmallsai/smLsbot",
    "bot_image_url": "https://raw.githubusercontent.com/therealsmallsai/smLsbot/main/assets/smlsbot.jpg",
}



def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "news-story"


def build_cards(cards: list[dict[str, str]]) -> str:
    rendered_cards: list[str] = []
    for card in cards:
        rendered_cards.append(
            f'''<div class="card p-6 border-l-{card.get("color", "cyan-500")}">\n'''
            f'''    <h4 class="font-bold text-{card.get("title_color", "cyan-400")} mb-2">[{card.get("label", "MALWARE MODULE")}]</h4>\n'''
            f'''    <p class="text-sm opacity-80">{card.get("body", "")}</p>\n'''
            "</div>"
        )
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">\n' + "\n".join(rendered_cards) + "\n</div>"


def build_hashtags(tags: list[str]) -> str:
    return "\n".join(
        f'<span class="text-[10px] bg-cyan-950 px-2 py-1 border border-cyan-800">#{tag}</span>'
        for tag in tags
    )


def build_terminal_log(lines: list[str]) -> str:
    return "<br>\n                        ".join(f"> {line}" for line in lines)


def load_story(path: Path | None) -> dict[str, Any]:
    if path is None:
        return dict(DEFAULT_STORY)

    payload = json.loads(path.read_text(encoding="utf-8"))
    merged = dict(DEFAULT_STORY)
    merged.update(payload)
    return merged


def render(template: str, story: dict[str, Any], display_date: str) -> str:
    replacements = {
        "{{PAGE_TITLE}}": story["page_title"],
        "{{BRAND_NAME}}": story["brand_name"],
        "{{SYSTEM_STATUS}}": story["system_status"],
        "{{REGION}}": story["region"],
        "{{THREAT_LEVEL}}": story["threat_level"],
        "{{DISPLAY_DATE}}": display_date,
        "{{FLASH_HEADLINE}}": story["flash_headline"],
        "{{FLASH_SUMMARY}}": story["flash_summary"],
        "{{PRIMARY_HEADLINE}}": story["primary_headline"],
        "{{PRIMARY_BODY}}": story["primary_body"],
        "{{MALWARE_CARDS}}": build_cards(story.get("cards", [])),
        "{{SPECIAL_SECTION_TITLE}}": story["special_section_title"],
        "{{SPECIAL_SECTION_BODY}}": story["special_section_body"],
        "{{TERMINAL_LOG}}": build_terminal_log(story.get("terminal_log", [])),
        "{{CTA_TEXT}}": story["cta_text"],
        "{{HASHTAGS}}": build_hashtags(story.get("hashtags", [])),
        "{{COPYRIGHT_TEXT}}": story["copyright_text"],
        "{{CONSOLE_NOTICE}}": story["console_notice"],
        "{{BOT_SECTION_TITLE}}": story["bot_section_title"],
        "{{BOT_NAME}}": story["bot_name"],
        "{{BOT_DESCRIPTION}}": story["bot_description"],
        "{{BOT_REPO_URL}}": story["bot_repo_url"],
        "{{BOT_IMAGE_URL}}": story["bot_image_url"],
    }

    output = template
    for key, value in replacements.items():
        output = output.replace(key, value)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--story-json", type=Path, help="Path to story JSON payload.")
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("tools/small-talk-news/templates/base_template.html"),
        help="Template path.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tools/small-talk-news/output"),
        help="Directory to write generated pages.",
    )
    parser.add_argument(
        "--timestamp",
        default=dt.datetime.now(dt.timezone.utc).strftime("%Y.%m.%d_%H:%M UTC"),
        help="Displayed timestamp for the header.",
    )

    args = parser.parse_args()

    story = load_story(args.story_json)
    template = args.template.read_text(encoding="utf-8")

    file_slug = slugify(story.get("primary_headline", "news"))
    output_path = args.output_dir / f"{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d-%H%M%S')}-{file_slug}.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(render(template, story, args.timestamp), encoding="utf-8")
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    main()
