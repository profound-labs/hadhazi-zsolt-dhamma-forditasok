all:
	pandoc \
		--output "Dharma-Tanitasok.epub" \
		--css "../assets/stylesheets/output-epub.css" \
		title.txt \
		dharma.md && \
	~/bin/epubcheck "Dharma-Tanitasok.epub"
