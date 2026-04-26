# Graph Report - literature-notes  (2026-04-24)

## Corpus Check
- 71 files · ~2,058,201 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1108 nodes · 2029 edges · 47 communities detected
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 329 edges (avg confidence: 0.78)
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
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 29|Community 29]]
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
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]

## God Nodes (most connected - your core abstractions)
1. `lower()` - 44 edges
2. `replace()` - 38 edges
3. `get()` - 36 edges
4. `now()` - 36 edges
5. `Path()` - 36 edges
6. `KnowledgeSynthesizer` - 33 edges
7. `set()` - 31 edges
8. `KnowledgeForest` - 30 edges
9. `KnowledgeForest` - 26 edges
10. `sub()` - 25 edges

## Surprising Connections (you probably didn't know these)
- `KnowledgeForest` --uses--> `Build knowledge forest from existing notes`  [INFERRED]
  knowledge_forest.py → tools/src/knowledge_graph/forest_builder.py
- `KnowledgeForest` --uses--> `Extract title from content or filename`  [INFERRED]
  knowledge_forest.py → tools/src/knowledge_graph/forest_builder.py
- `KnowledgeForest` --uses--> `Extract tags from content`  [INFERRED]
  knowledge_forest.py → tools/src/knowledge_graph/forest_builder.py
- `KnowledgeForest` --uses--> `Extract wikilinks from content`  [INFERRED]
  knowledge_forest.py → tools/src/knowledge_graph/forest_builder.py
- `KnowledgeForest` --uses--> `Create a sample data file for the web interface`  [INFERRED]
  knowledge_forest.py → tools/src/knowledge_graph/forest_builder.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (14): buildHTML(), buildHTMLUnbreakable(), commonjsRequire(), createCommonjsModule(), htmltag(), isLetter$2(), leastCommonAncestor(), node_path() (+6 more)

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (91): GitHubPagesGenerator, main(), Close database connection., Main CLI interface for GitHub Pages generation., Create CSS and JavaScript assets., Generates GitHub Pages compatible structure from Zettelkasten database., Generate complete GitHub Pages structure., Generate individual note pages. (+83 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (46): CleanKnowledgeForest, CleanNote, main(), Convert filename to clean ID, Create a better hash of content for deduplication, Find if this note is a duplicate of an existing one, Clean note representation with deduplication, Merge new note into existing note (+38 more)

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (63): addClass(), adjustSpacing(), Anchor(), arrayFrom(), assign(), attrInterpolate(), attrInterpolateNS(), bindKey() (+55 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (40): build_knowledge_forest(), create_sample_web_data(), extract_tags(), extract_title(), extract_wikilinks(), find_node_id(), main(), Extract title from content or filename (+32 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (41): copy_graph_to_pages(), Copy knowledge graph to GitHub Pages., count_notes(), generate_cse_readme(), generate_highlights_readme(), generate_main_index(), generate_sanskrit_readme(), get_note_titles() (+33 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (45): fix_control_characters(), fix_liquid_syntax(), fix_yaml_frontmatter(), main(), process_file(), Fix YAML frontmatter issues., Fix Liquid template syntax issues., Remove control characters that YAML doesn't like. (+37 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (28): KnowledgeForest, KnowledgeNode, KnowledgePathway, main(), Build semantic connections between nodes, Find semantic connections for a node, Extract key terms from content, Extract wiki-style links from content (+20 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (37): apply_changes(), backtick_line_ranges(), build_report(), build_targets(), Change, compile_title_pattern(), default_report_path(), extract_existing_link_targets() (+29 more)

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (20): main(), Note, Search notes by content or title., Get all notes with a specific tag., Get all tags with their counts., Get all notes linked from the given note., Get all notes that link to the given note., Convert database row to Note object. (+12 more)

### Community 10 - "Community 10"
Cohesion: 0.1
Nodes (20): buildTree(), color_formatHsl(), createTransformHooks(), defaultConstrain(), hex(), Hook, hsl(), hslConvert() (+12 more)

### Community 11 - "Community 11"
Cohesion: 0.12
Nodes (20): delayConstant(), delayFunction(), easeConstant(), get$1(), init(), Node(), onFunction(), parseTypenames$1() (+12 more)

### Community 12 - "Community 12"
Cohesion: 0.15
Nodes (10): main(), Generates client-side search functionality for GitHub Pages., Create additional search assets., Build mappings between file paths and URLs., Format frontmatter for Jekyll., Close database connection., Generate complete search functionality., Generate search index JSON file. (+2 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (19): attrConstant$1(), attrConstantNS$1(), attrFunction$1(), attrFunctionNS$1(), defaultView(), dispatchConstant(), dispatchEvent(), dispatchFunction() (+11 more)

### Community 14 - "Community 14"
Cohesion: 0.12
Nodes (17): attrTween(), durationConstant(), durationFunction(), easeVarying(), Namespace(), selection_attr(), set$1(), textConstant$1() (+9 more)

### Community 15 - "Community 15"
Cohesion: 0.19
Nodes (9): main(), Creates visualizations of the Zettelkasten knowledge graph., Generate an interactive HTML graph using D3.js., Generate a static network graph using NetworkX and Matplotlib., Get nodes and links data for visualization., Generate a hierarchical view of tags and their relationships., Close database connection., Main CLI interface for visualization. (+1 more)

### Community 16 - "Community 16"
Cohesion: 0.18
Nodes (15): check_container_logs(), check_docker_container(), check_internal_container_process(), check_port_usage(), create_simple_api_test(), main(), Test different API endpoints, Check if API process is running inside container (+7 more)

### Community 17 - "Community 17"
Cohesion: 0.24
Nodes (11): check_files(), main(), Check if required files exist, Test if a service is responding, Test smart query functionality, Test knowledge synthesis, Test system statistics, test_service() (+3 more)

### Community 18 - "Community 18"
Cohesion: 0.18
Nodes (12): array(), arrayAll(), constant(), inherit(), newId(), schedule(), selection_data(), selection_selectAll() (+4 more)

### Community 19 - "Community 19"
Cohesion: 0.2
Nodes (11): Color(), color_formatHex(), color_formatRgb(), hsla(), linear(), nogamma(), rgb(), rgb$1() (+3 more)

### Community 20 - "Community 20"
Cohesion: 0.2
Nodes (10): cosh(), datum(), dispatch(), interrupt(), Selection(), selection_interrupt(), sinh(), tanh() (+2 more)

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
Cohesion: 0.33
Nodes (6): createDependencyResolver(), createEntryMap(), getLoader(), hasKeys(), loadComponentsInOrder(), toSet()

### Community 26 - "Community 26"
Cohesion: 0.4
Nodes (2): add_to_bloom(), set_bit()

### Community 27 - "Community 27"
Cohesion: 0.6
Nodes (5): decodeEntity(), entity(), fromCodePoint(), isValidEntityCode(), replaceEntityPattern()

### Community 29 - "Community 29"
Cohesion: 0.5
Nodes (4): copyImageToClipboard(), createCanvas(), drawInlineSVG(), generateImage()

### Community 31 - "Community 31"
Cohesion: 0.67
Nodes (3): emphasis(), isAlphaNum(), scanDelims()

### Community 32 - "Community 32"
Cohesion: 0.67
Nodes (3): createSVG(), getComputedCss(), removeExistingSVG()

### Community 33 - "Community 33"
Cohesion: 0.67
Nodes (3): _arrayLikeToArray(), _createForOfIteratorHelperLoose(), _unsupportedIterableToArray()

### Community 34 - "Community 34"
Cohesion: 0.67
Nodes (3): isLetter(), replaceAt(), smartquotes()

### Community 35 - "Community 35"
Cohesion: 0.67
Nodes (3): assertSymbolNodeType(), checkDelimiter(), checkSymbolNodeType()

### Community 36 - "Community 36"
Cohesion: 0.67
Nodes (3): assertNodeType(), getHLines(), parseArray()

### Community 37 - "Community 37"
Cohesion: 0.67
Nodes (3): constant$2(), link(), linkHorizontal()

### Community 38 - "Community 38"
Cohesion: 0.67
Nodes (3): decompose(), parseCss(), parseSvg()

### Community 39 - "Community 39"
Cohesion: 0.67
Nodes (3): addAfter(), matchGrammar(), removeRange()

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (3): deflist(), markTightParagraphs$1(), skipMarker()

### Community 41 - "Community 41"
Cohesion: 0.67
Nodes (3): layoutChildren(), positionRoot(), shiftChange()

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (2): mclass_mathmlBuilder(), newDocumentFragment()

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (2): defineFunction(), defineFunctionBuilders()

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (2): exponential(), gamma()

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (2): getCharacterMetrics(), supportedCodepoint()

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (2): htmlblock(), isLetter$1()

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (2): scriptFromCodepoint(), SymbolNode()

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (2): create(), Timer()

## Knowledge Gaps
- **214 isolated node(s):** `Count markdown notes in each domain, excluding system directories.`, `Extract note titles from markdown files in directory.`, `Generate main INDEX.md with current statistics.`, `Generate CSE/README.md with current counts.`, `Generate sanskrit-lit/README.md with current counts.` (+209 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 26`** (6 nodes): `add_to_bloom()`, `calculate_bits()`, `get_bit()`, `membership()`, `set_bit()`, `bloom2.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `mclass_mathmlBuilder()`, `newDocumentFragment()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `defineFunction()`, `defineFunctionBuilders()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `exponential()`, `gamma()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (2 nodes): `getCharacterMetrics()`, `supportedCodepoint()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (2 nodes): `htmlblock()`, `isLetter$1()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (2 nodes): `scriptFromCodepoint()`, `SymbolNode()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (2 nodes): `create()`, `Timer()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `lower()` connect `Community 2` to `Community 0`, `Community 1`, `Community 4`, `Community 5`, `Community 7`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Why does `get()` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 7`, `Community 16`, `Community 17`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Why does `Path()` connect `Community 5` to `Community 0`, `Community 1`, `Community 2`, `Community 4`, `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 12`, `Community 17`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `lower()` (e.g. with `._path_to_id()` and `._classify_node_type()`) actually correct?**
  _`lower()` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Are the 22 inferred relationships involving `replace()` (e.g. with `get_note_titles()` and `._path_to_id()`) actually correct?**
  _`replace()` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `get()` (e.g. with `generate_main_index()` and `main()`) actually correct?**
  _`get()` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `now()` (e.g. with `generate_main_index()` and `generate_cse_readme()`) actually correct?**
  _`now()` has 30 INFERRED edges - model-reasoned connections that need verification._