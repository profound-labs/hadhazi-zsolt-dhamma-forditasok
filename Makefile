all:
	@cd ajahn-anan-tanitasai && make && cd .. && \
	cd ajahn-kalyano-tanitasai && make && cd .. && \
	cd dharma-tanitasok && make && cd .. && \
	echo "=== 📗 COMPLETED 📗 ==="
