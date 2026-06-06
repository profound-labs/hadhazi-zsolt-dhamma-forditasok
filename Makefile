all:
	@cd ajahn-anan-idezetek && make && cd .. && \
	cd ajahn-kalyano-idezetek && make && cd .. && \
	cd dharma-idezetek && make && cd .. && \
	echo "=== 📗 COMPLETED 📗 ==="
