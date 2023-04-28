# Adding content

First, Learn Markdown! Then, get yourself come toolings. 
If you are using [Visual Studio Code](https://code.visualstudio.com/) - which we recommend - these 2 plugins would sure help:

1. [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
2. [Mermaid Markdown Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=bpruitt-goddard.mermaid-markdown-syntax-highlighting)

## Learning materials
### Markdown
- [The Markdown Guide](https://www.markdownguide.org/)
- [Mastering Markdown (3 minute read)](https://guides.github.com/features/mastering-markdown/)

### MkDocs
- [Project documentation with Markdown](https://www.mkdocs.org/)
- [A Material Design theme for MkDocs](https://github.com/squidfunk/mkdocs-material)
- [A Mermaid graphs plugin for mkdocs](https://github.com/fralau/mkdocs-mermaid2-plugin)

### Diagrams
- [Mermaid](./tutorials/../mermaid.md)

## Writing documentation

Say, you want to add a new section on DataOS<sup>®</sup> Alerting capabilities. 
1. Create a new directory `alerts` under `/docs` 
2. Add a new file `index.md` under `/docs/alerts/`
3. Write your content in this file to your heart's content
4. Update `nav` section in `mkdocs.yaml` file to add this file to the navigation tabs
```
nav:
    - Alerts: alerts/index.md
```
5. Push your changes to the repo 
```
git add .
git commit -m 'your comments'
git push origin master
```