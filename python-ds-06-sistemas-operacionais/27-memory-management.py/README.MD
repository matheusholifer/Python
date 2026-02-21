Um código introdutório a Memory Management em python.

```python
import time

def tmm():
    blocos = []
    total_alocado = 0
    tamanho_bloco = 1024 * 1024  # 1 MB em bytes
    
    print("Iniciando alocação de memória...")
    
    try:
        while True:
            # Tenta alocar 1MB de bytes
            novo_bloco = bytearray(tamanho_bloco)
            blocos.append(novo_bloco)
            total_alocado += 1
            
            if total_alocado % 100 == 0:
                print(f"Alocados: {total_alocado} MB")
                
    except MemoryError:
        print("\n--- Memória Insuficiente! ---")
        print(f"Total final alocado: {total_alocado} MB")
        print("Mantenha o programa aberto para verificar o Monitor de Recursos.")
        print("Pressione Ctrl+C para encerrar.")
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    tmm()
```
