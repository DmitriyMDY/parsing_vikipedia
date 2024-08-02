import wikipediaapi

def print_paragraphs(page):
    paragraphs = page.text.split('\n\n')
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i+1}:\n{paragraph}\n")
        if (i + 1) % 3 == 0:
            choice = input("Продолжить листать параграфы (д/н)? ")
            if choice.lower() != 'д':
                break

def list_linked_pages(page):
    links = list(page.links.keys())
    for i, link in enumerate(links):
        print(f"{i + 1}: {link}")
    return links

def main():
    # Укажите user agent, заменив <YourAppName> и <your_email@example.com>
    user_agent = "MyWikipediaApp (contact: myemail@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(language='ru', user_agent=user_agent)
    query = input("Введите запрос: ")
    page = wiki_wiki.page(query)

    if not page.exists():
        print("Страница не найдена.")
        return

    while True:
        print("\nВыберите действие:")
        print("1: Листать параграфы текущей статьи")
        print("2: Перейти на одну из связанных страниц")
        print("3: Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == '1':
            print_paragraphs(page)
        elif choice == '2':
            links = list_linked_pages(page)
            link_choice = int(input("Введите номер связанной страницы: ")) - 1
            if 0 <= link_choice < len(links):
                page = wiki_wiki.page(links[link_choice])
                if not page.exists():
                    print("Страница не найдена.")
            else:
                print("Неверный выбор.")
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

