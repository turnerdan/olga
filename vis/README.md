# README: Illuminated Manuscript Feminine Smiley Face Prompt Template

**Overview**  
This README documents a flexible prompt template for generating an illuminated-manuscript–inspired **feminine** smiling face rich with data visualizations. The template is parameterized in two dimensions:

1. **Background States** (color, shape, complexity)  
2. **Face Variations** (makeup, hat, expression)

By substituting specific keywords into placeholders, you can produce multiple stylistic versions—each retaining the core “feminine smiley face with data charts” concept but varying in decorative flair or facial details.

---

## 1. Template Structure

At its core, the template consists of three parts:

1. **Parchment & Face Description**  
   - Aged parchment texture, gold accents, Gothic-era border  
   - Large circular **feminine** smiling face with chart-based eyes and mouth  
   - Interior filled with data visualizations (pie charts, bar graphs, line plots, etc.)

2. **Background Parameters**  
   - `BACKGROUND_COLOR`: warm tones or cool tones  
   - `BACKGROUND_SHAPE`: geometric patterns or organic flourishes  
   - `BACKGROUND_COMPLEXITY`: minimalist or highly elaborate

3. **Face Parameters**  
   - `FACE_MAKEUP`: presence/absence and style of decorative makeup  
   - `FACE_HAT`: headgear or none  
   - `FACE_EXPRESSION`: subtle smile, wink, surprised, etc.

Below is a generic prompt scaffold. Replace each uppercase placeholder with one of the example states defined in Sections 2 and 3.

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a flowing red line chart.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background with:
- Color: BACKGROUND_COLOR
- Shape: BACKGROUND_SHAPE
- Complexity: BACKGROUND_COMPLEXITY

On the face itself:
- Makeup: FACE_MAKEUP
- Hat: FACE_HAT
- Expression: FACE_EXPRESSION

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

## 2. Background States

Below are two example states for each background parameter. You can mix and match any of the choices to create **2 × 2 × 2 = 8** unique background combinations.

### 2.1 `BACKGROUND_COLOR`

- **Warm Tones**  
  > “Background awash in warm tones: deep crimson, burnt orange, and golden ochre washes, with subtle glowing highlights.”

- **Cool Tones**  
  > “Background rendered in cool tones: navy blue, emerald green, and violet washes, with silvery highlights.”

### 2.2 `BACKGROUND_SHAPE`

- **Geometric Patterns**  
  > “Background composed of repeating geometric patterns—interlocking circles, triangles, hexagons—in precise tessellations, each shape outlined in gold.”

- **Organic Flourishes**  
  > “Background of organic flourishes—flowing vines, curling tendrils, and leaf motifs—each curve accentuated in gold.”

### 2.3 `BACKGROUND_COMPLEXITY`

- **Minimalist**  
  > “Minimalist background: mostly blank parchment with only a faint wash of muted cream, a single thin gold border, and no additional ornamentation. Subtle calligraphic text in a single tiny panel.”

- **Highly Elaborate**  
  > “Highly elaborate background: densely layered ornamentation of scrolling vines, interlaced knotwork, miniature historiated scenes in each corner (monks illuminating texts, mythical beasts, scholars in lecture), tiny heraldic shields, delicate filigree, and multiple bands of gold leaf. Margins are filled with calligraphic Latin text, small marginalia figures, and additional border panels containing annotated data tables.”

---

## 3. Face Variations

These parameters describe how to adjust decorative details on the **feminine** smiling face itself. Combine any choice from each group for diverse results.

### 3.1 `FACE_MAKEUP`

- **No Makeup**  
  > “The face appears plain—no additional makeup, letting the natural parchment color show through around the charts. Feminine features include softly curved eyebrows and subtle lashes.”

- **Gilded Accents & Rouge**  
  > “The face is adorned with gilded filigree lines around the cheek areas (like illuminated marginalia), subtle rose-tinted rouge on the cheeks, delicate eyeliner framing the pie-chart eyes, and tiny gold dots above each eyebrow.”

### 3.2 `FACE_HAT`

- **No Hat**  
  > “No headgear is present; the circular feminine face sits directly on parchment, her gentle features unobscured.”

- **Medieval Scholar’s Cap**  
  > “A small, pointed medieval scholar’s cap (in dark blue velvet with gold trim) rests atop the circle, complementing her scholarly yet feminine demeanor.”

### 3.3 `FACE_EXPRESSION`

- **Standard Smiling**  
  > “A gently upward-curving red line chart forms a warm, straightforward smile framed by gently curved, feminine lips.”

- **Winking**  
  > “One pie-chart eye is slightly tilted and half-covered by a small gold crescent, suggesting a playful wink; the red line chart turns up in a flirtatious arc, accentuating her feminine charm.”

- **Surprised**  
  > “Both pie-chart eyes are wide (slightly enlarged), eyebrows arched, and the mouth is a small circular doughnut chart in deep red, indicating surprise—her feminine features highlighted by a slight blush.”

---

## 4. Example Prompts

Below are six complete example prompts showcasing different face parameters—each paired with a fixed background (“Warm Tones / Organic Flourishes / Highly Elaborate”). Feel free to swap out the background states as desired.

---

### Example 1: Plain Face, No Hat, Standard Smiling

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a flowing red line chart.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background of cool tones: navy blue, emerald green, and violet washes, with silvery highlights.
The background is composed of organic flourishes—flowing vines, curling tendrils, and leaf motifs—each curve accentuated in gold.
This background is highly elaborate: densely layered ornamentation of scrolling vines, interlaced knotwork, miniature historiated scenes in each corner (monks illuminating texts, mythical beasts, scholars in lecture), tiny heraldic shields, delicate filigree, and multiple bands of gold leaf. Margins are filled with calligraphic Latin text, small marginalia figures, and additional border panels containing annotated data tables.

On the face itself:
- Makeup: No Makeup
- Hat: No Hat
- Expression: Standard Smiling

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

### Example 2: Gilded Makeup, Scholar’s Cap, Winking

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a flowing red line chart.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background of warm tones: deep crimson, burnt orange, and golden ochre washes, with subtle glowing highlights.
The background is composed of geometric patterns—interlocking circles, triangles, hexagons—in precise tessellations, each shape outlined in gold.
This background is highly elaborate: densely layered ornamentation of scrolling vines, interlaced knotwork, miniature historiated scenes in each corner (monks illuminating texts, mythical beasts, scholars in lecture), tiny heraldic shields, delicate filigree, and multiple bands of gold leaf. Margins are filled with calligraphic Latin text, small marginalia figures, and additional border panels containing annotated data tables.

On the face itself:
- Makeup: Gilded Accents & Rouge
- Hat: Medieval Scholar’s Cap
- Expression: Winking

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

### Example 3: Gilded Makeup, No Hat, Surprised

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a small circular doughnut chart in deep red, indicating surprise.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background of cool tones: navy blue, emerald green, and violet washes, with silvery highlights.
The background is composed of organic flourishes—flowing vines, curling tendrils, and leaf motifs—each curve accentuated in gold.
This background is minimalist: mostly blank parchment with only a faint wash of muted cream, a single thin gold border, and no additional ornamentation. Subtle calligraphic text in a single tiny panel.

On the face itself:
- Makeup: Gilded Accents & Rouge
- Hat: No Hat
- Expression: Surprised

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

### Example 4: No Makeup, Scholar’s Cap, Standard Smiling

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a flowing red line chart.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background of warm tones: deep crimson, burnt orange, and golden ochre washes, with subtle glowing highlights.
The background is composed of geometric patterns—interlocking circles, triangles, hexagons—in precise tessellations, each shape outlined in gold.
This background is minimalist: mostly blank parchment with only a faint wash of muted cream, a single thin gold border, and no additional ornamentation. Subtle calligraphic text in a single tiny panel.

On the face itself:
- Makeup: No Makeup
- Hat: Medieval Scholar’s Cap
- Expression: Standard Smiling

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

### Example 5: No Makeup, No Hat, Winking

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a flowing red line chart.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background of cool tones: navy blue, emerald green, and violet washes, with silvery highlights.
The background is composed of geometric patterns—interlocking circles, triangles, hexagons—in precise tessellations, each shape outlined in gold.
This background is highly elaborate: densely layered ornamentation of scrolling vines, interlaced knotwork, miniature historiated scenes in each corner (monks illuminating texts, mythical beasts, scholars in lecture), tiny heraldic shields, delicate filigree, and multiple bands of gold leaf. Margins are filled with calligraphic Latin text, small marginalia figures, and additional border panels containing annotated data tables.

On the face itself:
- Makeup: No Makeup
- Hat: No Hat
- Expression: Winking

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

### Example 6: Gilded Makeup, Scholar’s Cap, Surprised

```
A richly detailed, hand-painted illuminated manuscript illustration on aged parchment:
a large circular **feminine** smiling face whose eyes are colorful pie charts and whose mouth is a small circular doughnut chart in deep red, indicating surprise.
The interior of the face is filled with varied data visualizations—bar graphs, scatterplots, area charts, and small tables—rendered in deep blues, reds, and greens with gold accents.

Surrounding the face is a background of warm tones: deep crimson, burnt orange, and golden ochre washes, with subtle glowing highlights.
The background is composed of organic flourishes—flowing vines, curling tendrils, and leaf motifs—each curve accentuated in gold.
This background is highly elaborate: densely layered ornamentation of scrolling vines, interlaced knotwork, miniature historiated scenes in each corner (monks illuminating texts, mythical beasts, scholars in lecture), tiny heraldic shields, delicate filigree, and multiple bands of gold leaf. Margins are filled with calligraphic Latin text, small marginalia figures, and additional border panels containing annotated data tables.

On the face itself:
- Makeup: Gilded Accents & Rouge
- Hat: Medieval Scholar’s Cap
- Expression: Surprised

Ornate medieval border of intertwining vines, floral motifs, and tiny historiated scenes (scribes, scholars, and mythical creatures) all accented in gold leaf.
Subtle calligraphic text in Latin script appears in miniature panels along the margins.
The overall style evokes a 14th-century Gothic illuminated manuscript that emphasizes feminine features such as gentle eyelashes, softly curved eyebrows, and delicate cheek highlights.
```

---

## 5. Usage Instructions

1. **Choose Background States**  
   - Select one option from each of the three background categories (Color, Shape, Complexity).  
   - Replace the placeholders `BACKGROUND_COLOR`, `BACKGROUND_SHAPE`, and `BACKGROUND_COMPLEXITY` in the scaffold with your chosen phrasing.

2. **Choose Face Variations**  
   - Decide whether the feminine smiley face wears makeup (`No Makeup` or `Gilded Accents & Rouge`).  
   - Decide on headgear (`No Hat` or `Medieval Scholar’s Cap`).  
   - Decide on expression (`Standard Smiling`, `Winking`, or `Surprised`).  
   - Replace `FACE_MAKEUP`, `FACE_HAT`, and `FACE_EXPRESSION` with your chosen descriptions.

3. **Compose Final Prompt**  
   - Paste the scaffold into your image-generation tool.  
   - Substitute each placeholder with the exact sentence or phrase from Sections 2 and 3.  
   - Run the prompt; adjust as needed for your model’s syntax requirements.

---

## 6. Tips & Best Practices

- **Maintain Consistency**: Keep the “face” text (charts, colors, gold accents, feminine features) exactly the same if you only want to vary backgrounds or facial accessories.  
- **Adjust Detail Level**: If your model struggles with dense decorative instructions, start with a “Minimalist” background and incrementally add detail.  
- **Combine Sparingly**: Too many conflicting descriptors (e.g., “geometric patterns” + “organic flourishes” in the same line) can confuse some generators. Stick to one choice per category.  
- **Test in Batches**: Run small tests (e.g., changing only the hat) to ensure each state change is correctly interpreted before combining all variations.

---

## 7. Summary

This template empowers you to generate a family of illuminated-manuscript–style **feminine** “data-rich” smiley faces. By varying three background parameters and three face parameters, you can create up to **48 unique permutations** (2 colors × 2 shapes × 2 complexities × 2 makeup × 2 hats × 3 expressions). The scaffold and examples above should serve as a clear guide to crafting exactly the look you want.

Feel free to expand by adding new hat styles (e.g., “crown of leaves”), makeup (e.g., “kohl-lined eyes”), or expressions (e.g., “raised eyebrow”). Each new variation follows the same placeholder-substitution pattern.
