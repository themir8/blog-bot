package bot

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/joho/godotenv"
	"github.com/parnurzeal/gorequest"
)

type User struct {
	UserID    int    `json:"user_id"`
	UserName  string `json:"username"`
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Phone     string `json:"phone"`
}

type BlogSubscribers struct {
	ID         int    `json:"id"`
	Subscriber string `json:"subscriber"`
	Blog       string `json:"blog"`
}

type Blog struct {
	ID              string            `json:"id"`
	Owner           string            `json:"owner"`
	Categories      []string          `json:"category"`
	BlogSubscribers []BlogSubscribers `json:"blogsubscribers"`
	Articles        string            `json:"articles"`
	Name            string            `json:"name"`
}

func Get_articles(user_id string) ([]interface{}, error) {
	err := godotenv.Load()
	if err != nil {
		return nil, err
	}

	url := os.Getenv("BASE_URL") + "/blog/" + user_id + "/"

	resp, _, errs := gorequest.New().Get(url).End()
	if errs != nil {
		err1 := errors.New("url: Url неправылно задан")
		return nil, err1
	}
	defer resp.Body.Close()
	var res map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&res)

	articles, exists := res["articles"].([]interface{})
	if !exists {
		return nil, nil
	}

	return articles, nil
}

func Get_blog_by_owner_id(user_id string) (*Blog, error) {
	err := godotenv.Load()
	if err != nil {
		return nil, err
	}

	url := os.Getenv("BASE_URL") + "/blog/" + user_id + "/"

	resp, _, errs := gorequest.New().Get(url).End()
	if errs != nil {
		err1 := errors.New("url: Url неправылно задан")
		return nil, err1
	}
	defer resp.Body.Close()

	var blog *Blog

	json.NewDecoder(resp.Body).Decode(&blog)

	for _, category := range blog.Categories {
		// if err != nil {
		// 	panic(err)
		// }
		fmt.Printf("%v\n", category)

	}
	return blog, nil
}

func (user *User) CreateUser() (int, error) {
	err := godotenv.Load()
	if err != nil {
		return 404, err
	}

	url := os.Getenv("BASE_URL") + "/user/"
	context := fmt.Sprintf(`{"user_id": %v, "username": %q, "first_name": %q, "last_name": %q, "phone": %q}\n`, user.UserID, user.UserName, user.FirstName, user.LastName, user.Phone)
	request := gorequest.New()
	// resp, body, errs := request.Post(url).
	_, _, errs := request.Post(url).
		Send(context).
		End()
	if errs != nil {
		log.Fatalln(errs)
	}
	return 201, nil
}
