package buttons

import (
	"fmt"

	"github.com/mirsaid-mirzohidov/blog-bot/bot/models"
	tele "gopkg.in/tucnak/telebot.v3"
)

func MainBtn(newbutton string) *tele.ReplyMarkup {
	menu := &tele.ReplyMarkup{ResizeKeyboard: true}
	var button tele.Row
	var button2 tele.Row
	btns1 := []string{"⭐️ Рекомендации", "👤 Подписки"}
	btns2 := []string{"🔍 Поиск"}
	if newbutton != "" {
		btns2 = append(btns2, newbutton)
	} else {
		fmt.Println("newbutton не задано")
	}
	for i := range btns1 {
		button = append(button, menu.Text(btns1[i]))
	}
	for i2 := range btns2 {
		button2 = append(button2, menu.Text(btns2[i2]))
	}
	menu.Reply(
		button,
		button2,
	)

	return menu
}

func GenerateBtn(texts []models.Articles) *tele.ReplyMarkup {

	gb := &tele.ReplyMarkup{ResizeKeyboard: true}
	var button tele.Row

	for _, text := range texts {
		button = append(button, gb.Text(text.Title))
	}
	button = append(button, gb.Text("Добавить статью"))
	gb.Reply(
		button,
	)

	return gb
}
