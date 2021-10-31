"use strict";

const morePostsButton = document.getElementById("more-posts");
const allPosts = document.getElementById("all-posts");

function getPosts(func) {
    const xhr = new XMLHttpRequest();

    xhr.open("GET", "/blog/load-more-posts");

    xhr.addEventListener("load", () => {
        const response = JSON.parse(xhr.responseText);
        func(response);
    });

    xhr.addEventListener("error", () => {
        console.log("error")
    });

    xhr.send();
}

function renderPosts(response) {
    const fragment = document.createDocumentFragment();
    response.forEach(post => {
        const card = document.createElement("div");
        if (post["last_post"] === "true") {
            card.classList.add("col");
            card.setAttribute("id", "last-post");
            card.setAttribute("data-last-id", `${post.id}`);
        } else {
            card.classList.add("col")
        }

    })
}
