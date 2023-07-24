<template>
  <div>
    <div class="category" v-for="items in category" :key="items">
      <div>{{ items.category_name }}</div>
      <button
        class="item-btn"
        v-for="supply in items.itemsCategory"
        :key="supply"
        @click="NavMenu(supply.id)"
      >
        <div class="item-cont">
          <div class="image-cont">
            <img class="image" :src="supply.image" alt="item-image" />
          </div>
          <div class="item-text">
            <div class="supply-name-cont">
              <h5 class="supply-name">{{ supply.name }}</h5>
            </div>
            <div class="total-cont">
              <h5>Total: {{ supply.total }}</h5>
            </div>
          </div>
        </div>
      </button>
    </div>
    <div class="return-box" @click="NavMenu()">
      <div></div>
    </div>
    <div class="nav-cont">
      <div></div>
    </div>
  </div>
</template>

<script setup>
let category = ref([]);
onMounted(() => {
  NavCont = document.querySelector(".nav-cont");
  returnbox = document.querySelector(".return-box");
  window.addEventListener("resize", () => {
    if (window.innerWidth > 1200) {
      NavCont.classList.remove("dismiss");
      NavCont.classList.remove("selected");
      returnbox.classList.remove("return-box-display");
      returnbox.classList.remove("return-box-nodisplay");
    }
  });
  fetch("http://127.0.0.1:8000/items/category/", {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      category.value = data;
    });
});

let NavCont = "";
let returnbox = "";
let currentItem = ref({});

function NavMenu(id) {
  if (NavCont.classList.contains("selected")) {
    NavCont.classList.remove("selected");
    NavCont.classList.add("dismiss");
    console.log("dismiss");
    returnbox.classList.remove("return-box-display");
    returnbox.classList.add("return-box-nodisplay");
  } else if (NavCont.classList.contains("dismiss")) {
    NavCont.classList.remove("dismiss");
    NavCont.classList.add("selected");
    console.log("selected");
    returnbox.classList.remove("return-box-nodisplay");
    returnbox.classList.add("return-box-display");
  } else if (
    !NavCont.classList.contains("dismiss") ||
    !NavCont.classList.contains("selected")
  ) {
    NavCont.classList.add("selected");
    console.log("selected");
    returnbox.classList.add("return-box-display");
  }
  fetch(`http://127.0.0.1:8000/items/CurrentItem/${id}`, {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      currentItem.value = data;
    });
}
</script>

<style scoped>
.item-btn {
  width: 20rem;
  height: 8rem;
}
.item-cont {
  width: 100%;
  height: 100%;
  background-color: rgb(223, 220, 220);
  opacity: 0.8;
  border: none;
  display: flex;
  flex-flow: row nowrap;
}
.image-cont {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 5rem;
  height: 8rem;
}
.image {
  width: 5rem;
  height: 5rem;
}
.item-text {
  width: 15rem;
  height: 8rem;
  display: flex;
  flex-flow: column nowrap;
}
.supply-name-cont {
  width: 15rem;
  height: 5rem;
}
.supply-name {
  font-size: 0.9rem;
  font-weight: 300;
}
.total-cont {
  width: 15rem;
  height: 3rem;
}

.return-box-display {
  display: display;
  position: absolute;
  top: 0%;
  left: 0%;
  height: 100vh;
  width: 100vw;
  opacity: 0.2;
  background-color: #6d7275;
}
.return-box-nodisplay {
  display: none;
  position: absolute;
  top: 0%;
  left: 0%;
  height: 100vh;
  width: 100vw;
  opacity: 0.2;
  background-color: #6d7275;
}
.selected {
  animation: slide-in 0.5s forwards;
  -webkit-animation: slide-in 0.5s forwards;
}

.dismiss {
  animation: slide-out 0.5s forwards;
  -webkit-animation: slide-out 0.5s forwards;
}
@keyframes slide-out {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-100%);
  }
}
@keyframes slide-in {
  0% {
    -webkit-transform: translateX(-100%);
  }
  100% {
    -webkit-transform: translateX(0%);
  }
}

.return-box-display {
  display: display;
  position: absolute;
  top: 0%;
  left: 0%;
  height: 100vh;
  width: 100vw;
  opacity: 0.2;
  background-color: #6d7275;
}
.return-box-nodisplay {
  display: none;
  position: absolute;
  top: 0%;
  left: 0%;
  height: 100vh;
  width: 100vw;
  opacity: 0.2;
  background-color: #6d7275;
}
</style>
