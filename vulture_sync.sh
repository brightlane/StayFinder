#!/bin/bash

# --- VULTURE SYNC PROTOCOL 2026 ---
# This script bypasses standard git limits for massive directory uploads.

REPO_URL="https://github.com/brightlane/SkyScanner.git"
COMMIT_MSG="VULTURE_SYNC_$(date +%Y%m%d_%H%M%S)"

echo "🦅 INITIALIZING VULTURE SYNC..."

# 1. Clean up Git index if it's lagging
git gc --prune=now --aggressive

# 2. Add files in batches to prevent memory overflow
echo "📦 STAGING NODES..."
git add index.html global_nodes.json robots.txt sitemap.xml
git add nodes/

# 3. Commit the payload
echo "💾 COMMITTING MILLION-NODE PAYLOAD..."
git commit -m "$COMMIT_MSG"

# 4. Force Push to BrightLane Repository
echo "🚀 EXECUTING FORCE PUSH TO SKYSCANNER..."
git push origin main --force

echo "✅ SYNC COMPLETE. THE MATRIX IS LIVE."
