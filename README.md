# Jingwu Tang’s personal website

An original, restrained academic homepage built with Jekyll and plain CSS. The homepage, CV, blog, and error page share the `folio` layout. They need no browser JavaScript, external font service, or CSS framework.

## Local preview

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Open `http://localhost:4000`. The development configuration skips remote GitHub metadata so preview works offline after dependencies are installed.

## Editing

- `_pages/about.md`: introduction, service, and personal notes.
- `_data/publications.yml`: papers, author order, venues, and links. Only entries marked `selected: true` appear on the homepage, in file order.
- `_pages/cv.md`: the CV overview page.
- `_pages/blog.html`: the blog list.
- `_layouts/post.html`: article layout and links between English and Chinese versions.
- `_layouts/folio.html`: shared document structure and navigation.
- `assets/css/folio.css`: typography, colors, spacing, responsive layouts, and print styles.
- `files/Jingwu_Tang_CV.pdf`: the public CV download.

The production configuration retains `https://tangjingwu.com` and GitHub Pages compatibility. Inherited demonstration pages are excluded from the generated website without deleting their source files.

## Blog

Keep drafts in the ignored `.private/blog/` directory. Finished posts belong in `_posts/YYYY-MM-DD-slug.md`; they use the `post` layout and `/blog/slug/` URLs automatically.

For English posts, set `lang: en`. A Chinese translation uses `lang: zh-CN`, `list_in_blog: false`, and its own `permalink`, such as `/blog/slug/zh/`. Each version declares `translation_url`, `translation_lang`, and `translation_label` to link to the other version. Dates use America/New_York. Posts dated in the future are omitted from normal builds.

Drafts are excluded from the public source and build. Publish a draft only when explicitly requested.

## CV source and public export

The canonical CV lives in the user’s Overleaf project. Its private Git URL is stored in the ignored `.cv-source` file. A local working copy is kept under `.private/overleaf-cv/`. The old root `cv.tex` is not authoritative.

After updating the Overleaf working copy, build a public PDF with an installed TeX distribution:

```sh
python3 scripts/export-cv.py .private/overleaf-cv
```

The exporter works on a temporary copy and includes only the professional email and website from the contact section. It leaves full contact details in the private source. Review the resulting PDF before publishing.

`.cv-source`, `.private/`, the old `cv.tex`, and local build files are ignored by Git. CV sources, local configuration, and helper scripts are also excluded from Jekyll output. Only the public PDF belongs in the site.

Keep Overleaf sources and local previews private. Push to Overleaf, change repository visibility, or rewrite history only when explicitly requested.

## Inherited files

Older source files and assets originated from [Academic Pages](https://academicpages.github.io/) and [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/). Their existing license is retained in `LICENSE`.
