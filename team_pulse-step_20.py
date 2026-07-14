# === Stage 20: Добавь восстановление записей из архива ===
# Project: TeamPulse
def restore_from_archive(self, archive_path):
        """Восстанавливает записи из текстового архива в формате TeamPulse."""
        if not os.path.exists(archive_path):
            print(f"Архив не найден: {archive_path}")
            return 0
        
        count = 0
        with open(archive_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                try:
                    parts = line.split('|||')
                    if len(parts) != 4:
                        print(f"Неверный формат строки в архиве: {line}")
                        continue
                    
                    date_str, title, mood_val, blockers = parts
                    date_obj = datetime.strptime(date_str.strip(), '%Y-%m-%d')
                    mood = int(mood_val.strip())
                    
                    entry = TeamPulseEntry(
                        date=date_obj,
                        title=title.strip(),
                        mood=mood,
                        blockers=[b.strip() for b in blockers.split(';') if b.strip()]
                    )
                    
                    self.entries.append(entry)
                    count += 1
                    
                except (ValueError, IndexError) as e:
                    print(f"Ошибка парсинга строки из архива: {line}: {e}")
        
        if count > 0:
            self.save()
        return count
