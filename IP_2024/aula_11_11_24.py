from loguru import logger
try:
    print(50/0)

except ZeroDivisionError as e:
    logger.error(f'erro de divisão por zero: {e}')
    logger.info('digite um divisor válido!')
except Exception as error:
    logger.error (f'error: {error}')

print("programa finalizado")