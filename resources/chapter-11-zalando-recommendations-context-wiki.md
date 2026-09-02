# Context Wiki: Commentary & Item Recommendations on Zalando

*A working knowledge base for context engineering — for any agent (human or AI) that has to decide what to show a customer and what to say about it.*

## 0. Why this document exists

Chapter 11 ("The Store That Builds Itself") argues that a recommendation surface should behave like a small scientific institution: it forms a hypothesis about the customer's **problem**, selects a **recommendation experience (RX)** to address it, and is honest about the strength of its evidence. This wiki is the reusable knowledge that hypothesis-forming step needs — the categories, personas, needs and style vocabulary an agent should reach for before it composes a page or writes a line of commentary.

It is written to be **used as context**, not read cover to cover: an agent generating a recommendation + commentary should pull the relevant persona, need, and style sections, check the writing guardrails, and produce output grounded in real signals rather than invented ones.

Everything below is one of two kinds of material:
- **Grounded fact** — sourced from search research (Zalando's own disclosures, engineering blog, published papers, or industry/UX research), with a source link.
- **Working hypothesis** — a naming scheme or heuristic this wiki proposes for practical use, flagged as such. Treat these the way Chapter 11 treats a problem fingerprint: a hypothesis to test against real behavior, not a fact about the customer.

## 1. Vocabulary (shared with Chapter 11)

| Term | Meaning |
|---|---|
| **Problem fingerprint** | A vector of *bounded problems* (comparison friction, size anxiety, etc.), each with an intensity, inferred from session signals. Not a personality label — local to this customer, this moment, this surface. |
| **RX (recommendation experience)** | A reusable capability — carousel, comparison, collage, finder, confidence/insight module — that knows what problem it addresses, when it's eligible, and how to configure itself. |
| **Commentary / insight RX** | An RX whose payload is *knowledge, not another candidate* — a sentence or module explaining *why* an item is shown, resolving fit/quality/trust uncertainty. This is the object this wiki is mainly in service of. |
| **Composer** | The layer that selects, configures, scores, and orders RXs into a page, accounting for saturation and synergy between them. |
| **Surface Value** | The (deliberately plural, non-single-scalar) objective the composer optimizes — different for item RXs (engagement, downstream action) than for insight RXs (read-through, decision confidence, return behavior). |
| **Coverage / Unmet demand** | Coverage: which known problems the current RX library *could* address. Unmet demand: which detected problems remain insufficiently addressed in production. |

Use this vocabulary when writing prompts, specs, or evals for recommendation agents — it keeps "commentary" from silently sliding into either generic ad copy or an unsupported personalization claim.

## 2. Category taxonomy

### 2.1 Top-level structure (grounded)

Zalando's catalog is organized first by shopper segment, then by product type, with several curated shopping formats layered on top of the core taxonomy.

- **Segments:** Women, Men, Kids. Women's assortment is the largest (~340k items; dominated by accessories/bags ~24%, shoes ~14%, tops ~11%); Men's (~190k items) is led by t-shirts/polos (~19%), bags/accessories (~18%), pants (~14%). [source](https://www.yocabe.com/en/which-products-to-sell-on-zalando-analysis-of-the-main-categories-of-items/)
- **Category groups within each segment:** clothing, shoes, accessories, sport, premium/designer, beauty (added 2018, still rolling out market by market — most recently Spain/Finland 2025). [source](https://ecommercegermany.com/blog/zalando-expands-southern-europe-launches-portugal-introduces-beauty-spain/)
- **Sport is not a flat category** — it's organized into "Worlds of Sport" hubs per activity (running, football, basketball, …), each with curated gear, inspiration, and advice — an editorial layer on top of the plain taxonomy. [source](https://corporate.zalando.com/en/fashion/going-extra-mile-zalando-inspires-customers-stay-active-sports-category)
- **Kids** is anchored by the in-house **Friboo** brand alongside third-party children's lines. [source](https://www.yocabe.com/en/which-products-to-sell-on-zalando-analysis-of-the-main-categories-of-items/)

### 2.2 Curated shopping formats layered on the taxonomy (grounded)

These matter for context engineering because they imply *different customer intent and different appropriate commentary tone* even for the same physical product:

- **Premium / Zalando Privé** — dedicated designer vertical; "premium brand additions" were explicitly credited as a 2024 growth driver, i.e. this is a strategic tier, not just a filter. [source](https://www.retail-insight-network.com/news/zalando-ends-2024-on-high-as-premium-brand-additions-pay-off/)
- **Zalando Lounge** — members-only flash-sale app, 2,500+ brands, up to 75% off, own plus-size and premium-outlet sub-sections. [source](https://play.google.com/store/apps/details?id=de.zalando.lounge)
- **Outlet** — physical + online off-price channel, 500+ brands, previous-season/single-size/minor-defect stock, now also carrying pre-owned and Beauty. [source](https://corporate.zalando.com/en/how-our-outlets-work)
- **Pre-owned** — formerly the standalone **Zircle** app (launched 2018), now folded into the core platform and Outlet stores rather than run separately. [source](https://ecommercenews.eu/zalando-discontinues-zircle/)
- **Private labels** (Anna Field, Even & Odd, Friboo, Pier One, Yourturn, Zign) function as an internal innovation lab — used to pilot things like adaptive fashion for people with disabilities before wider rollout. [source](https://www.fairwear.org/brands/zalando-se/) · [source](https://corporate.zalando.com/en/about-us/what-we-do/zalandos-private-labels)

### 2.3 Scale and marketplace structure (grounded)

Zalando connects **62M+ active customers** with **7,000+ brands** across **29 European markets**, and is shifting from primarily first-party retail toward a **Partner Program** (third-party brands list/fulfill directly) — reported above 40% of GMV, with a 2028 target of 40–50%. [source](https://corporate.zalando.com/en/investor-relations/zalando-full-year-2025-results) · [source](https://corporate.zalando.com/en/investor-relations/en/news-stories/zalando-expand-platform-business-support-brands-coronavirus)

**Implication for commentary:** an agent cannot assume uniform data quality or fulfillment behavior across items — a first-party item and a Partner Program item may have very different depth of size/fit history behind them, which should affect how confidently commentary makes a fit claim (see §6).

### 2.4 The underlying attribute layer (grounded)

- The catalog runs on a **Smart Product Platform** managing millions of products and thousands of structured attributes; as of 2025 Zalando reports **1.8M AI-enriched PDP attributes** — the taxonomy is now substantially machine-augmented, not hand-tagged. [source](https://engineering.zalando.com/posts/2017/10/zalando-smart-product-platform.html)
- Attribute modeling uses **ontology techniques** to encode which attributes are complementary vs. mutually exclusive (e.g. certain fits/colors/style tags cannot co-occur), improving tagging consistency. [source](https://engineering.zalando.com/posts/2018/03/semantic-web-technologies.html)
- A **Product Similarity Graph** + "Graph Browser" lets customers navigate by visual/semantic similarity via tags, as an alternate layer to the fixed category tree. [source](https://engineering.zalando.com/posts/2018/11/exploring-fashion-catalog.html)
- Partner-facing documentation calls a category an **"Outline"** and everything nested inside it (size, color, material, fit, …) an **"Attribute"** — useful shared vocabulary when writing specs that reference the catalog structure. [source](https://help.useresponse.com/hemi/knowledge-base/article/marketplaces-zalando-direct-connection-zalando-product-taxonomy_1)

## 3. Customer personas

### 3.1 Zalando's own published segmentation — "Z-Types" (grounded)

Zalando Media Solutions mined purchase patterns from 22M active customers (plus anonymized behavioral data) into **seven named behavioral archetypes**: **Happy Casuals, Fresh Families, Modern Mainstreamers, Hip Poppers, Street Snobs, Cultured Elite, Preppy Strivers.** [source](https://t3n.de/news/zalando-ztype-typologie-kunden-kaeufer-personas-915313/) · [source](https://geschaeftsbericht.zalando.de/2017/magazin/mission-ztypes-das-passende-marketing-fuer-jede-zielgruppe/)

This is the single most directly relevant artifact in this wiki: it is Zalando's own evidence that *behavior-derived* segments (not raw demographics) are the right unit for personalization at this company. Treat the seven Z-Types as the canonical starting taxonomy; treat everything else in this section as supplementary texture for building richer problem fingerprints within or across them.

### 3.2 Industry-standard behavioral personas (grounded, cross-retailer)

Each entry: persona → distinguishing **behavioral signal** (not demographic guess) → likely style/need cross-links.

| Persona | Behavioral signal | Cross-links |
|---|---|---|
| **Brand loyalist** | Low price sensitivity within owned brands, high repeat purchase, values consistency/VIP treatment over discounts. [source](https://1worldsync.com/resource-center/blog/shopper-persona-the-brand-loyalist/) | Return-hesitation is *low* here — trust is already established; commentary can reference brand-specific history directly. |
| **Deal hunter / bargain shopper** | No brand loyalty, multi-site price comparison, coupon-tool usage, purchase timed to sales calendar rather than product drop. [source](https://www.mytotalretail.com/article/optimize-e-commerce-sales-by-understanding-the-6-buyer-personas/) | Price/value uncertainty is the dominant need; outlet/Lounge surfaces are the natural home. |
| **Trend-seeker / fashion-forward** | High purchase frequency, low category affinity (buys across categories opportunistically), higher return rate; best evidenced indirectly via ASOS/H&M's Gen-Z-skewed high-frequency base and Zalando's own "Street Snobs" Z-Type. [source](https://businessmodelanalyst.com/hm-target-market-analysis/) | Discovery/exploration mission, not targeted search (§4.4); pairs with fast-rotating style aesthetics (§5.2). |
| **Capsule-wardrobe minimalist** | Low purchase frequency, high per-item consideration time, resistant to trend cycles; "capsule wardrobe" search interest spiked ~89% in a month. [source](https://en.wikipedia.org/wiki/Capsule_wardrobe) | Behavioral inverse of the trend-seeker — quality/durability commentary lands better than novelty framing. |
| **Sustainability-conscious** | Defined by actual filter/browsing behavior (sustainability filters, resale/rental engagement), *not* stated preference — 76% self-identify as conscious, only 38% actually shop that way; income doesn't predict this segment. [source](https://thesustainablefashionforum.substack.com/p/76-of-people-call-themselves-conscious) | Wants verifiable material/supply-chain detail, distrusts vague sustainability marketing (Gen Z: 45% actively worried about greenwashing). [source](https://lifestylemonitor.cottoninc.com/this-is-the-fiber-gen-z-prioritizes-while-embracing-authenticity-sustainability/) |
| **Plus-size / inclusive-sizing shopper** | Skews younger than assumed (55% of size 1X–3X buyers under 35); extended sizing lifts loyalty ~31%, purchase frequency ~24%; elevated "fit anxiety" from inconsistent sizing across brands drives higher try-before-buy/return propensity. [source](https://www.fastsimon.com/ecommerce-wiki/optimized-ecommerce-experience/supply-and-demand-challenges-in-the-womens-plus-size-market/) | Size-confidence commentary (§4.1) is the single highest-leverage RX for this persona. |
| **Athleisure shopper** | 45% buy online 3+ times/year, 22% YoY frequency growth; comfort (42%) and fit (16%) rank far above price (6th) as purchase drivers. [source](https://gearbunch.com/pages/athleisure-industry-statistics) | Low price sensitivity relative to general apparel; commentary can foreground comfort/performance attributes over discount framing. |
| **Luxury / premium — "absolute" vs. "aspirational"** | BCG-Altagamma: <1% of luxury buyers ("Top absolute", €50k+/yr) drive 23% of category value; "aspirational" buyers spend <€5k/yr occasionally. A quantified, spend-based split within one archetype. [source](https://web-assets.bcg.com/51/92/68b6af8346629c05e586a734d857/bcg-altagamma-true-luxury-global-consumer-insights-report-2025-vpress-final.pdf) | Maps to the Premium/Privé category tier (§2.2); commentary tone should shift from persuasive to purely informational (§6.1). |
| **Occasion / gift shopper** | Deadline-driven, narrow and fast session pattern triggered by an event (wedding, holiday), not steady seasonal browsing; needs distinct treatment from self-purchasers. [source](https://woveninsights.ai/site-blog/how-buyer-personas-change-based-on-seasonal-vs-occasion-based-shopping/) | Currently served mostly via curated editorial collections, not attribute filtering (§4.4) — a documented gap. |
| **Parent / family shopper** | Pragmatic, high-frequency replenishment driven by kids outgrowing sizes every 6–9 months; 93% research online first; pain points are cross-brand sizing inconsistency and stock mismatches. [source](https://www.giliguise.com/blogs/journal/parent-shopping-behavior-kids-clothes) | Repeat-purchase cadence tied to a *growth* cycle, not a trend cycle — commentary can safely reference "last time you sized up to X." |

**Working heuristic** (not sourced, proposed for practical use): the four most predictive behavioral metrics for placing a customer within this table, per a 2026 fashion-segmentation framework, are **purchase frequency, category affinity, days-since-last-purchase, and return rate**. [source](https://www.corradomanenti.it/en/behavioral-segmentation-in-fashion-a-2026-guide/) Use these four as the minimum signal set before attempting persona inference — a fingerprint built on fewer than these is closer to a guess than a hypothesis (see the Lea example, §8.3).

## 4. Customer needs / bounded problems

This section is the direct extension of Chapter 11's problem list (comparison friction, size anxiety, return hesitation, outfit visualization, filter fatigue, decision paralysis). Each entry adds the grounding evidence and the RX implication.

### 4.1 Size and fit anxiety — the dominant need

- Fit/sizing issues drive **~50–67% of fashion e-commerce returns**; "too small" alone is the single most common complaint (~34% of returns). Overall fashion return rates run 20–40%, vs. ~20% for e-commerce generally. [source](https://koozee.ai/blog/fashion-ecommerce-return-rate)
- **90% of apparel sites fail** to let users adequately judge look/size/fit before buying; 80%+ under-provide sizing information (Baymard Institute, 1,765 research hours, 18 sites, 370 sessions). [source](https://baymard.com/blog/apparel-ecommerce-ux-research-launch)
- **Bracketing** (ordering multiple sizes/colors to sort out fit at home, intending to return most) is now mainstream — up sharply from ~40% in 2018 — a customer-side workaround for a need the product experience doesn't solve directly. [source](https://eightx.co/blog/average-ecommerce-return-rate)
- Baymard recommends an **aggregate "fit" subscore** (runs small / true to size / runs large) distilled from reviews, separate from the general star rating — the specific evidence fit-anxious shoppers are hunting for and often can't find. [source](https://baymard.com/blog/apparel-provide-aggregate-fit-subscore-in-reviews)

**RX implication:** this is the highest-leverage insight-RX opportunity on the platform. Confidence language must be evidence-gated — see the fit-confidence writing rule in §6.2.

### 4.2 Comparison friction

Choice-overload research (Iyengar & Lepper's jam study, replicated in retail) shows large assortments draw more browsers but convert far worse than curated small sets (24-item display: 3% conversion vs. 6-item display: 30%). A study of 1.6M consumers attributed 64% of purchase-probability decline to shoppers avoiding search/comparison entirely when facing too many near-identical options. [source](https://www.crobox.com/blog/choice-overload)

**RX implication:** this is exactly Chapter 11's Mei case — the correct response is a comparison RX between the specific items the customer is actually deciding between, not more similar items.

### 4.3 Trust / quality uncertainty for unfamiliar brands

Word-of-mouth (89%) and reviews/ratings (85%) carry 2–3x the trust of brand advertising. Shoppers hitting a negative review often keep researching (nearly half) or cross-check other reviewers (over a third); a higher-rated, more-reviewed product beats a cheaper alternative in preference. [source](https://www.bazaarvoice.com/blog/why-customer-testimonials-and-peer-reviews-are-key-to-shopper-trust-in-2025/) Because shoppers can't touch fabric or check stitching online, they use **price/discount depth as a quality proxy** when a more direct signal is unavailable. [source](https://fashionandtextiles.springeropen.com/articles/10.1186/s40691-018-0128-2)

### 4.4 Discovery vs. targeted search — two different missions

Fashion shopping is often **exploratory**, not query-driven: customers arrive without a specific SKU in mind, searching by aesthetic ("quiet luxury," "coastal grandmother") rather than attribute. Sites optimized only for keyword search structurally miss this half of demand. [source](https://algonomy.com/blogs/ecommerce-product-discovery-optimization-fashion-retailers/) Occasion-based need (wedding guest, interview, vacation) is today served mainly through pre-curated editorial collections rather than structured occasion filtering — a documented gap for any occasion that doesn't match an existing collection (e.g. "beach wedding, humid, need to travel-pack it"). [source](https://www.theknot.com/content/where-to-buy-wedding-guest-dresses)

### 4.5 Filter fatigue / decision paralysis

Sites with weak filtering see **67–90% abandonment** among shoppers seeking a specific product type, vs. 17–33% on sites with strong filter/sort tooling. 38% of sites lack filters for attributes they display; 54% over-categorize (treating an attribute like color or fit as a top-level category rather than a filter), pushing shoppers into dead ends. [source](https://baymard.com/research/ecommerce-product-lists)

### 4.6 Return hesitation / value uncertainty

Resolving fit uncertainty **before checkout** measurably raises conversion and lowers returns — industry framing treats fit uncertainty as "not only a content problem — a data problem, a decision problem, and a confidence problem." [source](https://www.truefit.com/post/pdp-size-guidance-vs-fit-intelligence)

### 4.7 The JTBD frame — three simultaneous layers of need

Fashion purchases satisfy **functional** (cover/protect), **social** (fit in or stand out in a specific context), and **emotional** (feel confident) jobs at once — online and offline channels satisfy these differently (offline: tactile/emotional confidence; online: breadth and price comparison). A recommendation experience that only addresses the functional job while ignoring the social/emotional context (an interview, a wedding, a vacation) misses most of the actual motivation. [source](https://www.sciencedirect.com/science/article/abs/pii/S0969698922003149)

**Working checklist for an agent inferring a problem fingerprint:** for any detected need, ask which of functional / social / emotional it actually is — commentary that answers only the functional layer ("this is a jacket") when the real job is social ("will I look right at this event") will read as tone-deaf even if factually accurate.

## 5. Style archetypes

Two layers exist in the real world and both are useful, for different purposes.

### 5.1 Classic personal-styling typologies (grounded — stable, decades-old)

McJimsey's six archetypes (1960s) underpin most modern style quizzes; **Kibbe's** system (1987) is still in active use by image consultants: five core "essences" (**Classic, Romantic, Dramatic, Natural, Gamine**) plus hybrid subtypes, classified by body-line balance (soft/curved "Yin" vs. sharp/angular "Yang"), not size or weight. [source](https://theconceptwardrobe.com/kibbe-body-types/the-13-kibbe-body-types-their-clothing-lines)

| Archetype | Defining traits |
|---|---|
| **Classic** | Clean lines, symmetry, tailored fits, neutral/muted palette, quality fabric, minimal ornamentation. Favors investment pieces over trend-chasing. |
| **Romantic** | Soft/curved seams, chiffon/lace/velvet, florals, ruffles, fitted-but-flowing silhouettes. |
| **Dramatic** | Sharp vertical lines, architectural silhouettes, high-contrast/monochrome, statement accessories. |
| **Natural** | Loose/unconstructed fits, natural fibers (linen, cotton, suede), earthy tones, comfort and ease of movement prioritized. |
| **Gamine** | Mixed masculine/feminine, mixed delicate/bold in one outfit, graphic contrast, playful/quirky, trend-mixing. |

This layer is **stable** and good for a durable style preference signal (closer to Chapter 11's "durable characteristics" than to a situational one).

### 5.2 Modern aesthetic / microtrend taxonomies (grounded — fast-rotating)

A widely used consumer-facing "12 style aesthetics" framework and its neighbors, useful as the vocabulary customers themselves search with:

- **Minimalist / Clean Girl** — polished basics, neutral tones, simple fitted silhouettes.
- **Streetwear** — oversized graphics, cargo, chunky sneakers, comfort-as-self-expression.
- **Preppy** — Ivy-League crispness, blazers, loafers, pleated skirts, sweater vests.
- **Boho** — flowy fabric, layered jewelry, earthy tones, fringe/crochet.
- **Athleisure** — leggings/hoodies elevated with structured pieces for everyday wear.
- **Old Money / Quiet Luxury** — heritage tailoring, muted neutrals, no visible logos, restraint signals status.
- **Coastal Grandmother** — breezy linen, sundresses, straw accessories, pastel/cream/blue palette; softer and more lifestyle-driven than preppy.
- **Cottagecore / Dark Academia / Y2K / Coquette** — internet-native, TikTok/Instagram-driven, fast-rotating identity signals rather than durable wardrobes.
- **Grunge/Edgy** and **Business/Smart Casual** — occasion-adjacent tags (distressed denim/leather/dark palette vs. structured-but-not-suited workwear).

[source](https://whatcolorssuitme.com/aesthetics/) · [source](https://blog.depositphotos.com/modern-nostalgia-microtrends-aesthetics-2024.html)

**Working distinction (proposed):** treat §5.1 (Kibbe/McJimsey) as slow-moving *silhouette* preference and §5.2 as fast-moving *aesthetic/vocabulary* preference. A customer's fingerprint can carry one durable silhouette tag and one or more transient aesthetic tags simultaneously — they answer different questions ("what shape flatters/suits them" vs. "what look are they currently searching for").

### 5.3 How real styling services capture this (grounded — implementation patterns worth copying)

- **Stitch Fix:** doesn't assign one archetype. The quiz captures body type, waist level, body-part coverage preference, formal/casual leaning, color preference, risk tolerance, price sensitivity (plus optional linked Pinterest board); an algorithm combines up to five style types into a layered "StyleFile" a human stylist then uses. [source](https://www.stitchfix.com/how-it-works)
- **Trunk Club:** quiz (likes/dislikes, dimensions, favorite brands, budget) *plus* a Tinder-style "Style Swipes" thumbs up/down on garment images, refined continuously — a hybrid explicit + implicit signal approach. [source](https://www.mysubscriptionaddiction.com/trunk-club-mens-review)
- **Zalando itself:** a consumer style quiz sorts shoppers into broad types — *"Fashionable and On-trend," "Stylish and Elegant," "Curious and Unique," "Authentic and Relaxed"* — layered under an algorithmic personalization system ("Algorithmic Fashion Companion") plus a virtual fitting room. [source](https://www.appsflyer.com/blog/measurement-analytics/zalando-ai-fashion-personalization/)

**Implication:** don't force a single style label onto a customer. Model style as a *small weighted set* of tags (a handful of §5.1/§5.2 labels with intensities), the same way the problem fingerprint models needs — this is structurally the same idea Chapter 11 already uses for problems, just applied to taste.

## 6. Writing good commentary — the actionable playbook

This is the part meant to be pulled directly into an agent's system prompt or into an eval rubric for generated commentary.

### 6.1 Separate "explain" copy from "persuade" copy — don't write both in one sentence

The recommender-explanation literature identifies seven distinct explanation goals (transparency, scrutability, trust, persuasiveness, effectiveness, efficiency, satisfaction) that trade off against each other — you cannot maximize all of them in one line of copy. [source](https://link.springer.com/article/10.1007/s11280-021-00916-0) Transparency doesn't sell directly — it builds trust, which raises perceived value, which then drives purchase; salesy framing bolted onto an explanation undermines the mechanism it depends on. [source](https://acalytica.com/blog/ai-trust-buying-decisions)

**Rule:** decide, per piece of copy, whether it exists to *explain* (traceable to real data — write it plainly) or to *persuade* (styling enthusiasm — keep it clearly separate, e.g. a distinct sentence or tag, not interwoven with the evidentiary claim).

### 6.2 Fit-confidence language must be evidence-gated, never asserted flat

Zalando's own size/fit system (RecSys 2019 paper) derives personalized true-size predictions from a learned joint customer/article embedding space, not fixed brand charts, and its confidence should track real inputs — number of data points, recency, whether sizing was extrapolated across brands, and same-brand sizing consistency (this is literally how third-party fit-confidence engines like True Fit compute their score). [source](https://arxiv.org/pdf/1907.09844) · [source](https://www.truefit.com/how-it-works)

**Rule — hedge vocabulary tied to evidence tier** (proposed, follows UX confidence-communication research on graded verbal hedges over fake numeric precision [source](https://dl.acm.org/doi/10.1145/3816046.3816231)):

| Evidence available | Approved phrasing |
|---|---|
| High volume, recent, same-brand fit reports | "Runs true to size." |
| Some signal, but thin or mixed | "Fit reports are mixed — consider sizing up." |
| Extrapolated from other brands/products, or new item | "We don't have enough fit data on this one yet." |
| None | Say nothing about fit rather than invent a claim. |

A false fit claim is worse than no claim — this is a direct echo of Chapter 11's own Sami example ("the exact claim matters enormously because a false fit claim is worse than a mediocre recommendation").

### 6.3 Ground every personalization claim in a traceable input

Stitch Fix and Trunk Club notes are credible specifically because they reference something the customer recognizes giving the system — a saved item, a past return, a stated occasion — not generic flattery. [source](https://www.stitchfix.com/women/blog/inside-stitchfix/stitch-fix-note-request/) · [source](https://medium.com/unpacking-trunk-club/recommendation-systems-at-trunk-club-overview-part-1-cc5783e5ff4b) Making the data source legible ("based on the jackets you saved") rather than implying omniscient inference also avoids triggering the privacy-concern discount that otherwise offsets personalization's trust gain. [source](https://www.mdpi.com/2071-1050/18/2/1073)

**Rule:** every commentary sentence that implies "we know something about you" should be able to name, internally, the specific signal it's citing. If it can't, drop to population-level framing (§6.5).

### 6.4 Write in "help-seeker" voice, not "help-provider" voice

Explanation copy written in first person, offering a best guess ("I picked this because…") earns more trust than third-person, authoritative copy ("This is a great match for you because…"). [source](https://medium.com/@ekinceylan/explainable-recommendation-building-trust-for-algorithms-63ea7288a011) Pair explanatory copy with a lightweight correction affordance ("not quite my style" / edit-preference) where the surface allows it — scrutable systems that let the customer correct the reasoning build more durable trust than one-way justification. [source](https://arxiv.org/pdf/2410.19302)

### 6.5 Cold start: default to honest population-level framing, transition gradually

Standard practice for low-signal customers is showing genuinely popular/trending items with plain "popular this week" framing rather than fabricating a "picked for you" narrative — gate personalized-sounding phrasing behind an actual signal threshold. [source](https://www.mlwhiz.com/p/cold-start-problem-recsys-modern-approaches) An abrupt jump from generic to confidently-personalized copy reads as a "personality shift" and erodes trust in the system's consistency — transition the *language* gradually (population-level → "popular with people who liked X" → fully personalized) as evidence actually accumulates, matching the accumulation of real signal rather than jumping ahead of it. This is the direct implementation of Chapter 11's Lea principle: "Popular this week" can be a good statement when "we have inferred your soul from one click" is not.

### 6.6 Don't over-explain, and don't explain at the wrong moment

Surfacing "why" reasoning at non-critical decision points can *reduce* trust and slow decisions without raising perceived usefulness. [source](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2023.1151150/full) Reserve detailed rationale for the moments where the customer is actually deciding (hovering a size, near Add to Bag) rather than attaching an explanation to every single item card.

### 6.7 Keep tone consistent via an explicit style guide, not per-agent improvisation

Fashion copywriting best practice calls for an explicit tone-of-voice document (approved words, banned superlatives, tone variants for casual/sophisticated/playful contexts) applied consistently — Trunk Club maintained a public internal voice-and-tone guide for exactly this reason. [source](https://sites.google.com/a/trunkclub.com/copywriting-style-guide/voice-and-tone) When multiple agents or an LLM generate commentary, they should draw from one shared micro-style-guide (preferred fit-hedge phrases, banned superlatives, sentence-length norms) rather than each inventing tone independently.

## 7. What the system actually knows — grounding for what commentary can honestly claim

An agent should only claim what the underlying system plausibly has evidence for. Zalando's own published stack, for calibration:

- **Fashion DNA** — article embeddings ("fashion space") learned jointly from images/attributes and purchase likelihood; the substrate for item similarity and cold-start article mapping (new items get an embedding from content alone before any sales history exists). [source](https://research.zalando.com/project/fashion_dna/fashion_dna/)
- **LSTM dynamic customer model** — a per-customer "style vector" that drifts over time from purchase sequences, not a static preference snapshot — supports the "situational, not permanent" framing Chapter 11 insists on for problem fingerprints, and applies equally to style fingerprints. [source](https://arxiv.org/abs/1708.07347)
- **Size & fit model (RecSys 2019) + SizeNet** — personalized true-size prediction from a learned customer/article embedding space (not fixed charts); SizeNet extends this to brand-new items via image/metadata alone. An in-house ~80-person size-and-fit team; combined systems prevented ~8% of size-related returns in 2025. [source](https://arxiv.org/pdf/1907.09844) · [source](https://corporate.zalando.com/en/about-us/what-we-do/how-zalando-leverages-technology-help-customers-find-right-size)
- **Body-measurement-from-photo** — since July 2023, customers can get size guidance from two phone photos, matched against learned embeddings rather than self-reported measurements. [source](https://corporate.zalando.com/en/about-us/what-we-do/how-zalando-leverages-technology-help-customers-find-right-size)
- **Shop the Look / Outfit Generation** — complementary-item and outfit-composition models treating "does this set work together" as a distinct, combinatorial problem from single-item ranking. [source](https://engineering.zalando.com/posts/2018/09/shop-look-deep-learning.html) · [source](https://arxiv.org/pdf/2211.16353)
- **Homepage recsys moving from CTR to GNN-based** — an explicit, published acknowledgment that pure click-through optimization misses novelty, diversity, and "inspirational value," directly supporting §6.6's caution against over-indexing commentary on click-bait framing. [source](https://engineering.zalando.com/posts/2024/12/gnn-recommendations-zalando.html)
- **Zalando Assistant** — an LLM-powered conversational stylist combining Zalando's personalization stack with a third-party LLM, live in ~25 markets — the closest existing production analog to "commentary generation" as an RX. [source](https://corporate.zalando.com/en/technology/zalando-launch-fashion-assistant-powered-chatgpt)
- **Discovery Feed** (2025) — a personalized content+commerce feed positioning Zalando as a "daily lifestyle companion," reported reaching 9M+ weekly users — evidence the company is already betting on inspiration/discovery surfaces (§4.4), not just transactional ones. [source](https://corporate.zalando.com/en/technology/zalando-progresses-inspiration-entertainment-mission-ai-powered-discovery-feed)

**Rule:** commentary should never claim a capability stronger than what a system like this plausibly supports (e.g., don't claim "we know exactly how this fits your body" from a partner-program item with no fit history — see §2.3).

## 8. Step-by-step process for a recommendation + commentary agent

1. **Read the signals available**, not more. Minimum viable fingerprinting signal set: purchase frequency, category affinity, days-since-last-purchase, return rate (§3.2), plus session-level behavior (repeat visits, filtering, comparison switching, size-chart opens, basket adds/removals) as in Chapter 11.
2. **Infer a problem fingerprint** — a small weighted set of bounded needs from §4, each with an intensity, not a single funnel-stage label.
3. **Infer a style fingerprint** — a small weighted set of tags from §5.1 (durable silhouette) and §5.2 (current aesthetic), not a single archetype forced onto the customer.
4. **Cross-check against the persona table (§3)** as a sanity check, not a source of truth — the persona is a lens for noticing gaps, the fingerprint is what actually drives the page.
5. **Select the RX**, not just the item. Ask: is the dominant need actually "more items" (retrieval/ranking problem), or is it comparison, confidence, visualization, or trust (an insight/commentary problem)? Chapter 11's rule applies directly: if the problem is comparison friction, a ranked list is the wrong species of answer.
6. **Check evidence tier before writing any claim** — especially fit (§6.2) and personalization (§6.3). If evidence is thin, downgrade the phrasing; never downgrade to silence-that-implies-confidence.
7. **Write the commentary** using §6's rules: help-seeker voice, one job per sentence (explain xor persuade), traceable signal, calibrated hedge, consistent tone from the shared style guide.
8. **Log the trace** — which signals were read, which problem/style tags were inferred, which RXs were eligible, which won and lost, and why. Chapter 11: "why did this page exist" must always have a better answer than "the model chose it."
9. **Define the success signal before serving** — for an insight RX this is read-through / decision confidence / return-rate change, not click-through (§6.6, §7's GNN note).

## 9. Worked examples

### 9.1 Mei — comparison friction (from Chapter 11, extended)

Signals: repeat visits to two specific trail-shoe PDPs over 5 days, fast switching, one saved, declining time-on-page. Fingerprint: comparison friction (high), price-quality confusion (moderate). Style: Natural/Athleisure. RX: a direct comparison of the two shoes on the attributes her behavior indicates matter, then a confidence module on the remaining uncertainty; generic similar-items demoted, not removed. Commentary: "You've been comparing these two — here's how they actually differ on cushioning and durability, since that's what you've been checking." (traceable signal, help-seeker voice, no fabricated fit claim.)

### 9.2 Sami — size anxiety, non-shoppable answer

Signals: size selected, size chart opened twice, unfamiliar brand, no add-to-bag. Fingerprint: size anxiety (high), return hesitation (moderate), brand trust (low). RX: an insight module, not another carousel — evidence about how similarly-sized buyers fit this specific item, gated by real evidence tier (§6.2). If the brand is a recent Partner Program addition with thin fit history, the honest phrasing is "we don't have enough fit data on this one yet," paired with a generic size-chart aid rather than a confident claim.

### 9.3 Lea — honest cold start

Signals: arrived from a social link, no account, no session depth — below the minimum viable signal set in §8.1. Fingerprint: none reliably inferable. RX: population-level framing per §6.5 — "Popular this week in [category]" anchored on the opened product, season, and location; avoid any "picked for you" phrasing. As she generates more signal within the session (a filter applied, a second product opened), the composer can graduate toward "popular with people who also looked at X," never jumping straight to fully personalized language.

### 9.4 A new example — the plus-size occasion shopper

Signals: filtered to extended sizing, opened three "wedding guest" curated collection items, opened size chart on each, added and removed one item from basket. Persona cross-check: plus-size/inclusive-sizing (§3.2) intersecting occasion shopper (§3.2). Fingerprint: size anxiety (high, compounded by inconsistent cross-brand plus-size charts per §3.2), occasion fit (high — social/emotional job per §4.7, not just functional). Style: whatever aesthetic tag her viewed items cluster around (e.g. Romantic per §5.1). RX: fit-confidence commentary scoped specifically to plus-size reviewers of that item (an aggregate fit subscore per §4.1) plus an occasion-framed collage rather than a generic size-chart link — because the emotional job here ("will I look right at this wedding") is at least as load-bearing as the functional one.

## 10. Guardrails / anti-patterns

- **Don't** turn the persona table (§3) into a permanent label on the customer. Chapter 11: "I do not want the system deciding that Hani is metaphysically a `RETURN_HESITANT_PERSON`... Some characteristics are durable. Many are situational."
- **Don't** write a fit or quality claim the system has no evidence for (§6.2) — a false claim is worse than no claim.
- **Don't** conflate explanation and persuasion in one sentence (§6.1) — it weakens both and risks reading as a dark pattern (persuasive-explanation research shows framing measurably shifts choices independent of item merit). [source](https://www.sciencedirect.com/science/article/pii/S1071581925002757)
- **Don't** optimize commentary RXs for click-through — an insight module that works perfectly may get zero clicks while quietly resolving the customer's actual blocker (Chapter 11's Sami point, §6.6, §7).
- **Don't** treat occasion-based need as solved by having *a* curated collection — check whether the collection actually matches the customer's specific occasion constraints (§4.4) before assuming coverage.
- **Don't** assume uniform data depth across the catalog — Partner Program items may carry thinner fit/quality history than first-party or established private-label items (§2.3, §7).
- **No silent caps:** if commentary generation is limited (only top-N items get a note, no re-generation on stockout, sampling for cost reasons), that limitation should be visible in the trace (§8.8), not hidden behind confident-sounding output for the items that did get covered.

## 11. Source index

All sources cited inline above; the six research passes behind this document, for anyone extending it:
1. Zalando category taxonomy and catalog engineering (Smart Product Platform, ontology, similarity graph).
2. Fashion-specific customer personas and segmentation (Zalando Z-Types, McKinsey, BCG-Altagamma, Baymard, industry blogs).
3. JTBD and UX friction in online fashion (Baymard apparel research, choice-overload studies, JTBD academic literature).
4. Style archetype taxonomies (Kibbe/McJimsey, modern aesthetics, Stitch Fix/Trunk Club/Zalando profiling implementations).
5. Explainable-recommendation and styling-commentary best practice (HCI/recsys literature, Stitch Fix/Trunk Club practice, True Fit confidence framing, cold-start UX).
6. Zalando's own published recommendation engineering (Fashion DNA, LSTM customer model, size/fit ML, Shop the Look, GNN homepage work, Zalando Assistant, Discovery Feed).
