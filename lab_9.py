def build_transition_table(needle):
    m = len(needle)
    # Знайдемо всі унікальні символи в needle, щоб не будувати таблицю для всього алфавіту
    alphabet = set(needle) 
    
    # Створюємо список словників. Індекс списку - це поточний стан.
    # transition_table[state][char] = next_state
    transition_table = [{} for _ in range(m + 1)]
    
    for state in range(m + 1):
        for char in alphabet:
            # Моделюємо ситуацію: ми мали збіг довжиною `state` і побачили символ `char`
            current_string = needle[:state] + char
            
            # Шукаємо найдовший префікс needle, який збігається з кінцем current_string
            next_state = 0
            # Перевіряємо всі можливі довжини від найбільшої до найменшої
            for k in range(min(m, len(current_string)), 0, -1):
                if current_string.endswith(needle[:k]):
                    next_state = k
                    break
            
            transition_table[state][char] = next_state
            
    return transition_table
def fsm_search(haystack, needle):
    if not needle:
        return [] # Якщо шукана стрічка порожня
    
    # 1. Будуємо таблицю
    transition_table = build_transition_table(needle)
    m = len(needle)
    
    state = 0
    indices = []
    
    # 2. Проходимо по тексту
    for i, char in enumerate(haystack):
        # Якщо символ є в нашій таблиці (тобто він зустрічається в needle)
        if char in transition_table[state]:
            state = transition_table[state][char]
        else:
            # Якщо символу немає в needle, автомат скидається в стан 0
            state = 0
            
        # Якщо ми досягли стану, що дорівнює довжині needle — ми знайшли збіг!
        if state == m:
            # Вираховуємо індекс початку збігу
            start_index = i - m + 1
            indices.append(start_index)
            
    return indices
