package models

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

type Articles struct {
	ID         string `json:"id"`
	Title      string `json:"title"`
	Text       string `json:"text"`
	Category   string `json:"category"`
	Author     string `json:"author"`
	Blog       string `json:"blog"`
	PostedDate string `json:"posted_date"`
	EditedDate string `json:"edited_date"`
}

type Blog struct {
	ID              string            `json:"id"`
	Owner           string            `json:"owner"`
	Categories      []string          `json:"category"`
	BlogSubscribers []BlogSubscribers `json:"blogsubscribers"`
	Articles        []Articles        `json:"articles"`
	Name            string            `json:"name"`
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
	resp, _, errs := request.Post(url).
		Send(context).
		End()
	if resp.StatusCode != 201 {
		fmt.Println(resp.Status)
	}
	if errs != nil {
		log.Fatalln(errs)
		err1 := errors.New("Error in post request")
		return 500, err1
	}
	return 201, nil
}

func Get_articles(user_id string) (*Blog, error) {
	err := godotenv.Load()
	if err != nil {
		return nil, err
	}

	url := os.Getenv("BASE_URL") + "/blog/" + user_id + "/"

	resp, _, errs := gorequest.New().Get(url).End()
	if errs != nil {
		err1 := errors.New("url: Url неправылно задан " + os.Getenv("BASE_URL"))
		return nil, err1
	}
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		fmt.Println(resp.Status)
	}
	var article *Blog
	err = json.NewDecoder(resp.Body).Decode(&article)
	if err != nil {
		fmt.Println(err)
		return nil, err
	}

	articles := article

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
