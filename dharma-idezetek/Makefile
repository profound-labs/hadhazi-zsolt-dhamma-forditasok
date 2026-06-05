all:
	pandoc \
		--output "Dharma Tanítások.epub" \
		--css "../assets/stylesheets/output-epub.css" \
		title.txt \
		dharma.md && \
	~/bin/epubcheck "Dharma Tanítások.epub"
