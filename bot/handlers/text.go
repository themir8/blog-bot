package handlers

import (
	"log"
	"strconv"

	"github.com/mirsaid-mirzohidov/blog-bot/bot/buttons"
	"github.com/mirsaid-mirzohidov/blog-bot/bot/models"
	tele "gopkg.in/tucnak/telebot.v3"
)

func OnText(c tele.Context) error {
	chat := c.Sender()

	articles, err := models.Get_articles(strconv.Itoa(chat.ID))
	if err != nil {
		log.Println(err)
		return err
	}
	text := "Список ваших статей:\n\n"
	for i, article := range articles.Articles {
		text += strconv.Itoa(i) + " " + article.Title + "\n"
	}
	switch c.Message().Text {
	case "Мой блог":
		c.Send(text, buttons.GenerateBtn(articles.Articles))
	default:
		c.Send("/start")
	}
	return nil
}
