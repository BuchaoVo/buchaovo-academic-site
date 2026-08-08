# buchaovo.com — open academic website

A complete, static, open-source academic website starter for **research identity, research programs, publications, open-source scientific tools, research notes, and structured reading notes**.

Stack:

- [Quarto](https://quarto.org/) for content and static-site generation
- GitHub for source control
- GitHub Actions for continuous integration and deployment
- GitHub Pages for hosting
- Huawei Cloud DNS for `buchaovo.com`

No database, CMS, application server, or cloud credentials are required.

## 1. Repository structure

```text
.
├── _quarto.yml
├── index.qmd
├── about.qmd
├── research/
├── publications/
├── tools/
├── notes/
├── reading/
├── _templates/
├── bibliography/
├── assets/
├── scripts/
└── .github/workflows/
```

The content model is deliberate:

- **Research**: organized by scientific questions/programs.
- **Publications**: formal papers/preprints and associated artifacts.
- **Tools**: reusable scientific software.
- **Notes**: your original research/technical reasoning.
- **Reading**: notes centered on external papers.

## 2. Local prerequisites

Install Quarto from the official website, then verify:

```bash
quarto --version
```

Python is optional. It is only needed for the helper scripts included in this template.

## 3. Personalize the starter

Run:

```bash
python scripts/bootstrap.py \
  --name "Your Name" \
  --github "your-github-user" \
  --orcid "0000-0000-0000-0000" \
  --email "you@example.com"
```

Then manually review:

- `_quarto.yml`
- `index.qmd`
- `about.qmd`
- `CITATION.cff`
- starter pages containing `REPLACE`

Optionally add a public CV at `assets/cv.pdf`, then add a CV button/link to `index.qmd`.

## 4. Preview locally

```bash
quarto preview
```

or:

```bash
make preview
```

Build without starting a server:

```bash
quarto render
```

The generated site is written to `_site/` and is intentionally ignored by Git.

## 5. Add content

Copy a file from `_templates/`, or use the helper:

```bash
python scripts/new_content.py publication "My paper title" --slug my-paper
python scripts/new_content.py tool "My Tool" --slug my-tool
python scripts/new_content.py note "Robust design evaluation" --slug robust-evaluation
python scripts/new_content.py reading "Paper title" --slug paper-short-name
```

All content pages use directory-style URLs, e.g.:

```text
/publications/my-paper/
/tools/my-tool/
/notes/robust-evaluation/
```

## 6. Create the GitHub repository

Create a repository such as:

```text
buchaovo/buchaovo-academic-site
```

Then:

```bash
git init
git add .
git commit -m "Initial academic website"
git branch -M main
git remote add origin git@github.com:buchaovo/buchaovo-academic-site.git
git push -u origin main
```

The repository can be public under the MIT license. Review all content before publishing; an open repository makes source files public as well as the rendered site.

## 7. Enable GitHub Pages

In the GitHub repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Open the **Actions** tab and verify that `Deploy Quarto site to GitHub Pages` succeeds.

The deploy workflow:

1. checks out `main`;
2. installs Quarto;
3. runs `quarto render`;
4. uploads `_site/` as the GitHub Pages artifact;
5. deploys it to the `github-pages` environment.

Pull requests run a separate render-only check and cannot deploy.

## 8. Configure the custom domain first in GitHub

Before changing DNS, configure/verify the domain in GitHub to reduce domain-takeover risk.

In **Settings → Pages → Custom domain**, enter:

```text
buchaovo.com
```

GitHub's custom Actions deployment does not require a repository `CNAME` file; the custom domain is configured in repository settings.

Also use GitHub's domain verification feature when available for your account.

## 9. Huawei Cloud DNS records for buchaovo.com

In Huawei Cloud DNS, remove any conflicting old records for the apex domain, then create these records.

### Apex domain

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

### www

| Type | Name | Value |
|---|---|---|
| CNAME | `www` | `buchaovo.github.io` |

Do **not** use a wildcard `*` DNS record for GitHub Pages.

The site is configured with `buchaovo.com` as the canonical domain. With both the apex and `www` records configured, GitHub Pages can redirect the alternate hostname to the configured canonical hostname.

DNS propagation is not instantaneous. Verify records after saving them:

```bash
dig buchaovo.com +short
dig www.buchaovo.com +short
```

On Windows PowerShell you can use `Resolve-DnsName` instead of `dig`.

## 10. HTTPS

After DNS resolves correctly, return to **Settings → Pages** and enable **Enforce HTTPS** when GitHub makes the option available.

Do not add a separate reverse proxy, Cloudflare proxy, or Huawei CDN until the basic GitHub Pages deployment is working. Add those later only for a specific performance or access requirement.

## 11. Publication and copyright hygiene

For your own papers, host only versions permitted by the journal/publisher agreement. For other authors' papers, link to canonical DOI, PubMed, arXiv, or publisher pages rather than copying publisher PDFs into this repository.

For each serious software project, keep the actual software in its own repository. The page under `/tools/` should be the stable academic landing page linking documentation, releases, paper, and citation metadata.

## 12. Recommended release checklist

Before calling the site public:

- [ ] Replace all `YOUR ...`, `REPLACE`, and `ADD_URL` placeholders.
- [ ] Delete the example publication/tool/reading pages or replace them with real content.
- [ ] Add 2–3 real Research pages.
- [ ] Add all public publications.
- [ ] Optionally add a public CV and link it from the site.
- [ ] Confirm ORCID, Scholar, GitHub, and email links.
- [ ] Run `quarto render` locally.
- [ ] Push and confirm both GitHub Actions workflows are green.
- [ ] Configure `buchaovo.com` in GitHub Pages before changing DNS.
- [ ] Configure Huawei Cloud DNS.
- [ ] Verify `https://buchaovo.com` and `https://www.buchaovo.com`.
- [ ] Enable HTTPS.
- [ ] Review the public repository for accidental secrets or private research data.

## 13. Design principle

The site should answer four questions quickly:

1. What problems do you study?
2. What have you published?
3. What reusable tools have you built?
4. What technical knowledge have you made publicly useful?

Avoid turning the home page into a chronological blog feed. Keep the home page curated and let Quarto listings automatically maintain the deeper collections.

## License

Website infrastructure/template code is released under the MIT License. Your own papers, figures, notes, datasets, and other research content may require separate copyright/license notices as appropriate.
