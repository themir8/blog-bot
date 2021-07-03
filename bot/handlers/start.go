package handlers

import (
	"github.com/mirsaid-mirzohidov/blog-bot/bot/buttons"
	"github.com/mirsaid-mirzohidov/blog-bot/bot/models"
	tele "gopkg.in/tucnak/telebot.v3"
)

func OnStart(c tele.Context) error {
	chat := c.Sender()
	user := models.User{UserID: chat.ID, UserName: chat.Username, FirstName: chat.FirstName, LastName: chat.LastName, Phone: "998998141352"}

	user.CreateUser()
	c.Send("<b>Hello</b>", buttons.MainBtn("Мой блог"))
	return nil
}
