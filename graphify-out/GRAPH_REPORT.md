# Graph Report - literature-notes  (2026-04-24)

## Corpus Check
- 70 files · ~2,056,879 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1079 nodes · 1950 edges · 39 communities detected
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 306 edges (avg confidence: 0.78)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]

## God Nodes (most connected - your core abstractions)
1. `lower()` - 44 edges
2. `replace()` - 37 edges
3. `get()` - 36 edges
4. `now()` - 36 edges
5. `Path()` - 34 edges
6. `KnowledgeSynthesizer` - 33 edges
7. `KnowledgeForest` - 30 edges
8. `set()` - 29 edges
9. `KnowledgeForest` - 26 edges
10. `sub()` - 23 edges

## Surprising Connections (you probably didn't know these)
- `Build knowledge forest from existing notes` --uses--> `KnowledgeForest`  [INFERRED]
  tools/src/knowledge_graph/forest_builder.py → knowledge_forest.py
- `Extract title from content or filename` --uses--> `KnowledgeForest`  [INFERRED]
  tools/src/knowledge_graph/forest_builder.py → knowledge_forest.py
- `Extract tags from content` --uses--> `KnowledgeForest`  [INFERRED]
  tools/src/knowledge_graph/forest_builder.py → knowledge_forest.py
- `Extract wikilinks from content` --uses--> `KnowledgeForest`  [INFERRED]
  tools/src/knowledge_graph/forest_builder.py → knowledge_forest.py
- `Create a sample data file for the web interface` --uses--> `KnowledgeForest`  [INFERRED]
  tools/src/knowledge_graph/forest_builder.py → knowledge_forest.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (28): buildHTML(), buildHTMLUnbreakable(), commonjsRequire(), create(), createCommonjsModule(), defineFunction(), defineFunctionBuilders(), exponential() (+20 more)

### Community 1 - "Community 1"
Cohesion: 0.04
Nodes (48): CleanKnowledgeForest, CleanNote, main(), Convert filename to clean ID, Create a better hash of content for deduplication, Find if this note is a duplicate of an existing one, Clean note representation with deduplication, Merge new note into existing note (+40 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (44): Close database connection., count(), nap(), now(), poke(), sleep(), timerFlush(), wake() (+36 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (41): build_knowledge_forest(), create_sample_web_data(), extract_tags(), extract_title(), extract_wikilinks(), find_node_id(), main(), Extract title from content or filename (+33 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (35): generate_synthesis_report(), KnowledgeSynthesizer, Extract key concepts from a collection of notes, Extract main topics from notes based on titles and tags, Synthesizes knowledge from notes to create insights and connections, Find connections between a set of notes, Build a synthesis group starting from a seed note, Generate a summary of knowledge in a specific domain (+27 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (43): addClass(), adjustSpacing(), arrayFrom(), assign(), children(), childSelector(), createAliasResolver(), createDependencyResolver() (+35 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (26): KnowledgeForest, KnowledgeNode, KnowledgePathway, main(), Build semantic connections between nodes, Find semantic connections for a node, Extract key terms from content, Extract wiki-style links from content (+18 more)

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (32): copy_graph_to_pages(), Copy knowledge graph to GitHub Pages., Find notes that match a wikilink., count_notes(), generate_cse_readme(), generate_highlights_readme(), generate_main_index(), generate_sanskrit_readme() (+24 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (35): check_container_logs(), check_docker_container(), check_internal_container_process(), check_port_usage(), create_simple_api_test(), main(), Test different API endpoints, Check if API process is running inside container (+27 more)

### Community 9 - "Community 9"
Cohesion: 0.06
Nodes (39): fix_control_characters(), fix_liquid_syntax(), fix_yaml_frontmatter(), main(), process_file(), Fix YAML frontmatter issues., Fix Liquid template syntax issues., Remove control characters that YAML doesn't like. (+31 more)

### Community 10 - "Community 10"
Cohesion: 0.06
Nodes (37): Anchor(), array(), arrayAll(), _arrayLikeToArray(), attrInterpolate(), attrInterpolateNS(), bindKey(), childFind() (+29 more)

### Community 11 - "Community 11"
Cohesion: 0.06
Nodes (37): attrTween(), delayConstant(), delayFunction(), durationConstant(), durationFunction(), easeConstant(), easeVarying(), get$1() (+29 more)

### Community 12 - "Community 12"
Cohesion: 0.09
Nodes (19): main(), Note, Search notes by content or title., Get all notes with a specific tag., Get all tags with their counts., Get all notes linked from the given note., Get all notes that link to the given note., Convert database row to Note object. (+11 more)

### Community 13 - "Community 13"
Cohesion: 0.09
Nodes (18): GitHubPagesGenerator, main(), Main CLI interface for GitHub Pages generation., Create CSS and JavaScript assets., Generates GitHub Pages compatible structure from Zettelkasten database., Generate complete GitHub Pages structure., Generate individual note pages., Generate a single note page. (+10 more)

### Community 14 - "Community 14"
Cohesion: 0.1
Nodes (23): cosh(), creator(), datum(), dispatch(), dragDisable(), inherit(), interrupt(), newId() (+15 more)

### Community 15 - "Community 15"
Cohesion: 0.15
Nodes (10): main(), Generates client-side search functionality for GitHub Pages., Create additional search assets., Build mappings between file paths and URLs., Format frontmatter for Jekyll., Close database connection., Generate complete search functionality., Generate search index JSON file. (+2 more)

### Community 16 - "Community 16"
Cohesion: 0.13
Nodes (19): attrConstant$1(), attrConstantNS$1(), attrFunction$1(), attrFunctionNS$1(), defaultView(), dispatchConstant(), dispatchEvent(), dispatchFunction() (+11 more)

### Community 17 - "Community 17"
Cohesion: 0.17
Nodes (9): LinkApplicator, main(), Apply links to multiple files, Save a detailed log of all changes, Load the missing links suggestions from JSON, Create a backup of the file before modifying, Add wiki-style links around unlinked mentions of target, Apply suggested links to a single file (+1 more)

### Community 18 - "Community 18"
Cohesion: 0.19
Nodes (9): main(), Creates visualizations of the Zettelkasten knowledge graph., Generate an interactive HTML graph using D3.js., Generate a static network graph using NetworkX and Matplotlib., Get nodes and links data for visualization., Generate a hierarchical view of tags and their relationships., Close database connection., Main CLI interface for visualization. (+1 more)

### Community 19 - "Community 19"
Cohesion: 0.16
Nodes (14): Color(), color_formatHex(), color_formatHsl(), color_formatRgb(), hsl(), hsla(), hslConvert(), linear() (+6 more)

### Community 20 - "Community 20"
Cohesion: 0.22
Nodes (6): buildTree(), cleanNode(), Hook, transform(), transform$1(), transform$2()

### Community 21 - "Community 21"
Cohesion: 0.38
Nodes (6): create_api_integration(), main(), Create API integration files for your Jekyll site, Update site navigation to include API features, Main integration function, update_navigation()

### Community 22 - "Community 22"
Cohesion: 0.33
Nodes (7): classArray(), classedAdd(), classedFalse(), classedRemove(), classedTrue(), classList(), selection_classed()

### Community 23 - "Community 23"
Cohesion: 0.29
Nodes (7): distributeExtra(), moveSubtree(), nextLContour(), nextRContour(), separate(), setLThr(), setRThr()

### Community 24 - "Community 24"
Cohesion: 0.33
Nodes (6): interpolateNumber(), interpolateString(), interpolateTransform(), one(), x(), zero()

### Community 25 - "Community 25"
Cohesion: 0.4
Nodes (2): add_to_bloom(), set_bit()

### Community 26 - "Community 26"
Cohesion: 0.6
Nodes (5): decodeEntity(), entity(), fromCodePoint(), isValidEntityCode(), replaceEntityPattern()

### Community 28 - "Community 28"
Cohesion: 0.5
Nodes (4): copyImageToClipboard(), createCanvas(), drawInlineSVG(), generateImage()

### Community 30 - "Community 30"
Cohesion: 0.67
Nodes (3): layoutChildren(), positionRoot(), shiftChange()

### Community 31 - "Community 31"
Cohesion: 0.67
Nodes (3): assertSymbolNodeType(), checkDelimiter(), checkSymbolNodeType()

### Community 32 - "Community 32"
Cohesion: 0.67
Nodes (3): emphasis(), isAlphaNum(), scanDelims()

### Community 33 - "Community 33"
Cohesion: 0.67
Nodes (3): decompose(), parseCss(), parseSvg()

### Community 34 - "Community 34"
Cohesion: 0.67
Nodes (3): constant$2(), link(), linkHorizontal()

### Community 35 - "Community 35"
Cohesion: 0.67
Nodes (3): createSVG(), getComputedCss(), removeExistingSVG()

### Community 36 - "Community 36"
Cohesion: 0.67
Nodes (3): assertNodeType(), getHLines(), parseArray()

### Community 37 - "Community 37"
Cohesion: 0.67
Nodes (3): createTransformHooks(), setPlugins(), wrapFunction()

### Community 38 - "Community 38"
Cohesion: 0.67
Nodes (3): isLetter(), replaceAt(), smartquotes()

### Community 39 - "Community 39"
Cohesion: 0.67
Nodes (3): deflist(), markTightParagraphs$1(), skipMarker()

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (3): addAfter(), matchGrammar(), removeRange()

## Knowledge Gaps
- **214 isolated node(s):** `Count markdown notes in each domain, excluding system directories.`, `Extract note titles from markdown files in directory.`, `Generate main INDEX.md with current statistics.`, `Generate CSE/README.md with current counts.`, `Generate sanskrit-lit/README.md with current counts.` (+209 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 25`** (6 nodes): `add_to_bloom()`, `calculate_bits()`, `get_bit()`, `membership()`, `set_bit()`, `bloom2.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `lower()` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 6`, `Community 7`, `Community 13`, `Community 17`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `Path()` connect `Community 7` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 6`, `Community 8`, `Community 9`, `Community 12`, `Community 13`, `Community 15`, `Community 17`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Why does `now()` connect `Community 2` to `Community 0`, `Community 3`, `Community 4`, `Community 6`, `Community 7`, `Community 13`, `Community 14`, `Community 17`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `lower()` (e.g. with `._path_to_id()` and `._classify_node_type()`) actually correct?**
  _`lower()` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `replace()` (e.g. with `get_note_titles()` and `._path_to_id()`) actually correct?**
  _`replace()` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `get()` (e.g. with `generate_main_index()` and `main()`) actually correct?**
  _`get()` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `now()` (e.g. with `generate_main_index()` and `generate_cse_readme()`) actually correct?**
  _`now()` has 30 INFERRED edges - model-reasoned connections that need verification._