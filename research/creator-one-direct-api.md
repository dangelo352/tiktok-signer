# TikTok One creator direct-API research

## Finding

The in-app Creator Marketplace / TikTok One campaign surface is an H5 client.
Its current creator-center bundle calls same-origin `/CreativeOne/...` routes;
these are not the consumer Android `/aweme/v1/...` endpoints targeted by this
repository's Argus/Gorgon/Ladon signer.

Inside TikTok, the H5 request layer uses the native `x.request` bridge. The
bridge receives the relative URL, HTTP method, query/body fields, and two safe
configuration flags (`needCommonParams` and JSON formatting). In a normal web
browser, the fallback uses `fetch` with `credentials: "include"`. No X-Bogus,
Argus, Gorgon, or Ladon construction appears in the creator bundle's request
layer. This makes session reuse—not signature generation—the main problem for
a direct campaign scraper.

Static inspection of TikTok 46.3.3 on the connected Android device narrows the
gap further. The bridge routes requests through TikTok's Retrofit/TTNet stack,
adds `request_tag_from=lynx` to the query and `x-tt-dataflow-id=671088913` to
the headers, and obtains the creator account's `X-Tt-Token` from TikTok's
account service. TTNet can then attach its normal device signatures. This
repository can supply the signature family, but a valid creator token remains
required; signatures plus an unrelated TikTok Ads browser cookie are not a
substitute for that token.

The live US mobile host observed on the device is
`https://inapp-ttp2.tiktokv.us`. The same creator homepage route also responds
on `https://ads.us.tiktok.com` to an existing TikTok One web session, which is
useful for a cookie-based replay client.

## Campaign-management read path

The collaboration stage values embedded in the bundle are:

| Value | Stage |
| ---: | --- |
| 1 | Todo |
| 2 | Pending |
| 3 | Collaborating |
| 4 | Done |

The minimum read-only crawl is:

1. `GET /CreativeOne/OrderQuery/CreatorCampaignManagementHomepage`
2. For each stage, paginate `GET /CreativeOne/OrderQuery/CreatorCollabList`
   with `collabStage`, `page`, `limit`, and optional `campaignID`.
3. Hydrate each row through
   `GET /CreativeOne/OrderQuery/CreatorGetCollabDetailV2`.
4. Fetch linked order, file, post, analytics, tracking, or generated-content
   records only when their IDs are present.

Primary read endpoints and inputs:

| Endpoint | Query fields |
| --- | --- |
| `CreatorCampaignManagementHomepage` | none |
| `CreatorCollabList` | `collabStage`, `limit`, `page`, `campaignID` |
| `CreatorGetCollabDetailV2` | `campaignID`, `opportunityID`, `orderID`, `creatorAgencyID`, `joinSource`, `partnerCampaignID` |
| `CreatorGetOrderDetail` | `orderID` |
| `CreatorGetFolderTree` | `campaignID` |
| `CreatorGetFileList` | `campaignID`, `folderID`, `orderType`, `limit`, `page` |
| `CreatorGetPostItemList` | `page`, `limit`, `scene`, `orderID`, `brandLinkID` |
| `CreatorAnalyticOrderInfo` | `itemID`, `videoID` |
| `CreatorGetOrderTrackingInfo` | `orderID` |
| `CreatorGetGeneratedContent` | `campaignID`, `generateAction`, `taskID` |

## Reproducing the inventory

Download the current creator-center JavaScript referenced by the TikTok One H5
page, then run:

```bash
python tools/extract_creator_one_api.py creator-center.js --format markdown
```

To retain every `/CreativeOne/...` route constant in the bundle—not just the
wrappers whose HTTP method and input object can be proved—add
`--include-unwrapped`. Unknown methods remain labeled `UNKNOWN`:

```bash
python tools/extract_creator_one_api.py creator-center.js \
  --include-unwrapped --format markdown
```

The extractor is deliberately static and secret-safe. Live validation still
requires an authenticated TikTok session from the device or browser. POST
routes include both searches and mutations; do not replay them merely because
they are present in the inventory.

For a captured H5 session, the guarded proof-of-concept client can call only
the campaign-related GET allowlist:

```bash
python tools/creator_one_readonly.py homepage --cookie-file /secure/session-cookie.txt
python tools/creator_one_readonly.py collabs \
  --cookie-file /secure/session-cookie.txt \
  --param collabStage=1 --param page=1 --param limit=20
```

It can also consume the existing scraper's JSON session format without
printing the cookie:

```bash
python tools/creator_one_readonly.py homepage \
  --session-json /secure/tiktok-api-session.json
```

The client rejects unknown parameters, has no arbitrary URL mode, never sends
POST requests, and does not print the session cookie or error response bodies.
