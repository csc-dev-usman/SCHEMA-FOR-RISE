# Rise First-Page Allowed Modules V1.0

**Status:** `HOMEPAGE_SCHEMA_PROFILE_ADDED_NO_SCHEMA_OUTPUT`

---

## Purpose

This document defines the allowed future schema modules for the Rise FC homepage (route `/`) and specifies what evidence is required before each module may be emitted in a schema output. These modules are authorized for future consideration only. PR #4 emits no schema.

---

## Allowed future first-page modules

The following four modules are the authorized future targets for `HOMEPAGE_SCHEMA_PROFILE`:

- `Organization`
- `WebSite`
- `WebPage`
- `BreadcrumbList`

**Allowed does not mean emitted.** Emission requires a completed evidence map, an approved operator prompt, passing validation, and explicit controller approval. None of these exist after PR #4.

---

## Module-by-module requirements

### Organization

**Purpose in homepage schema:** Identifies the sports organization (Rise FC) as the structured entity behind the website.

**Required evidence before emission:**

| Evidence category | Requirement |
|------------------|-------------|
| Approved organization identity | Club name and/or legal name confirmed from Phase 0 |
| Approved site/name identity | Organization name traceable to Phase 0 |
| Approved canonical URL/domain | Primary domain confirmed from Phase 0 or page evidence |
| Contact fields | All held — do not emit phone, email unless owner-approved |
| sameAs / social URLs | All held — do not emit any sameAs value unless owner-approved |
| Logo URL | Held — do not emit absolute logo URL unless owner-approved |
| Schema description | Held — do not emit description from tagline or mission line unless owner-approved |
| Founder/founding date | Held unless Phase 0 explicitly confirms |
| Address/place identity | Held — blocked until separately approved |

**Hold rule:** If any held field is requested for Organization, omit the field. Do not infer or guess values.

---

### WebSite

**Purpose in homepage schema:** Identifies the website associated with the organization.

**Required evidence before emission:**

| Evidence category | Requirement |
|------------------|-------------|
| Approved website identity | Website name confirmed from Phase 0 or page evidence |
| Approved canonical site URL | Primary domain confirmed — must be stable, not a redirect or CMS preview |
| Approved site name | Site name traceable to Phase 0 or confirmed page title |
| SearchAction | Held — do not emit unless separately authorized in a later doctrine PR |

**Hold rule:** Do not invent the canonical URL. If the canonical domain is not confirmed from Phase 0 or observable page evidence, hold.

---

### WebPage

**Purpose in homepage schema:** Identifies the homepage as a specific web page within the site.

**Required evidence before emission:**

| Evidence category | Requirement |
|------------------|-------------|
| Approved homepage identity | Homepage confirmed as the target page for this profile |
| Approved canonical homepage URL | Canonical URL for `/` confirmed from Phase 0 or page evidence |
| Approved page title/name evidence | Page title or name traceable to Phase 0 or confirmed page content |
| Approved page relationship to website | `isPartOf` relationship to WebSite confirmed |
| breadcrumb | Only via BreadcrumbList — do not duplicate in WebPage unless validator confirms safe |

**Hold rule:** Do not use a CMS-generated or guessed canonical URL. Confirm from Phase 0 or observable page evidence.

---

### BreadcrumbList

**Purpose in homepage schema:** Provides structured breadcrumb navigation data for the homepage.

**Required evidence before emission:**

| Evidence category | Requirement |
|------------------|-------------|
| Approved page route | Route `/` confirmed |
| Approved homepage breadcrumb item | Homepage breadcrumb item confirmed from page evidence |
| Approved canonical URL | Canonical URL for homepage item confirmed |
| Breadcrumb hierarchy | Only one level for homepage — do not invent nested hierarchy |

**Hold rule:** Do not invent a breadcrumb hierarchy. The homepage has a single breadcrumb item. Do not add items not supported by confirmed page structure.

---

## Required evidence before emission

All four allowed modules share these global pre-emission requirements:

1. Homepage evidence map exists and is approved (later PR)
2. Operator prompt for `HOMEPAGE_SCHEMA_PROFILE` exists and is approved (later PR)
3. Truth fingerprint verified: `80edd829806cae271242c6a8e853edabdb8b2f16ca5a8fa1a3fc69ff5b78d53d`
4. No held fields emitted without owner approval
5. No blocked modules included
6. Validator protocol run and passing (later PR)
7. Controller/human approval granted (later PR)

---

## Non-authorization

This document does not authorize JSON-LD generation. It does not authorize schema output. It does not authorize current website implementation or Astro attachment.

---

## Hold rules

| Condition | Rule |
|-----------|------|
| Evidence map missing | HOLD — do not draft any module |
| Operator prompt missing | HOLD — do not draft any module |
| Fingerprint mismatch | HOLD — do not proceed |
| Held field requested | HOLD — omit the field. Do not estimate. |
| Blocked module requested | HOLD — reject. Do not include. |
| Phase 0 / page evidence conflict | HOLD — escalate upstream |
| Canonical URL not confirmed | HOLD — do not invent |
| Controller approval missing | HOLD — do not proceed to output |
