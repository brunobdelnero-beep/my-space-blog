# Brainstorm Warning ⛈️

A static blog for weekly class posts, built for GitHub Pages.

## 📁 File Structure

```
Blog/
├── index.html          # About Me page
├── posts.html          # Posts listing page
├── posts/              # Individual blog posts
│   └── week-1.html     # Example first post
├── css/
│   └── style.css       # All styles
└── README.md           # This file
```

## 🚀 Deploying to GitHub Pages

1. Create a new repository on GitHub
2. Push this folder to the repository
3. Go to Settings → Pages
4. Under "Source", select "Deploy from a branch"
5. Select `main` branch and `/ (root)` folder
6. Click Save
7. Your site will be live at `https://yourusername.github.io/repository-name/`

## ✍️ Adding a New Post

### Step 1: Create the post file

1. Copy `posts/week-1.html`
2. Rename it to `week-X.html` (where X is the week number)
3. Edit the content:
   - Update the `<title>` tag
   - Change the week number and date
   - Change the post title
   - Write your content in the `post-body` section

### Step 2: Add to posts listing

Open `posts.html` and add a new card in the `posts-grid` section:

```html
<article class="post-card" style="animation-delay: 0.2s;">
    <div class="post-meta">
        <span class="post-week">Week X</span>
        <span class="post-date">Your Date Here</span>
    </div>
    <h2 class="post-title">
        <a href="posts/week-X.html">Your Post Title</a>
    </h2>
    <p class="post-excerpt">
        Brief description of your post...
    </p>
    <a href="posts/week-X.html" class="read-more">Read more →</a>
</article>
```

### Step 3: Commit and push

```bash
git add .
git commit -m "Add week X post"
git push
```

## 🎨 Customization

### Update About Me

Edit `index.html`:
- Change "Your Name" to your actual name
- Update the details (Currently, Studying, Interests)
- Add your own bio text
- Replace the 📸 emoji with an actual image if desired

### Change Colors

Edit `css/style.css` and modify the CSS variables at the top:

```css
:root {
    --color-accent: #c45d3a;      /* Main accent color (terracotta) */
    --color-bg: #faf6f1;          /* Background color */
    /* ... other variables */
}
```

### Add an Image

To add your photo to the About page:

1. Add your image to the Blog folder (e.g., `photo.jpg`)
2. In `index.html`, replace:
```html
<div class="about-image-placeholder">
    <span>📸</span>
</div>
```
With:
```html
<img src="photo.jpg" alt="Your Name" style="width: 200px; height: 200px; object-fit: cover; border-radius: 16px;">
```

## 📝 Writing Tips

- Use `<h2>` for section headings
- Use `<p>` for paragraphs
- Use `<ul>` or `<ol>` for lists
- Use `<blockquote>` for quotes
- Use `<strong>` for bold and `<em>` for italics

## 🔗 Useful Links

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

---

Expect scattered ideas ⚡
