<template>
  <div>
    <div class="open-menu-cont">
      <button class="open-menu-btn" @click="NavMenu">
        <div class="open-menu-icon-cont">
          <font-awesome-icon :icon="['fas', 'bars']" class="open-menu-icon" />
        </div>
      </button>
    </div>
    <div class="return-box" @click="NavMenu">
      <div></div>
    </div>
    <div class="nav-cont">
      <div>
        <div class="user">
          <div class="user-icon-cont">
            <font-awesome-icon :icon="['fas', 'user']" class="user-icon" />
          </div>
          <div class="user-info">
            <h2 class="user-title">My Account</h2>
            <h3 class="username">user1234@gmail.com</h3>
          </div>
        </div>
        <div class="menu-container">
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'boxes-stacked']"
                class="catalog-icon"
              />
            </div>
            <h3 class="tag">CATALOG</h3>
          </button>
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'hand-holding-hand']"
                class="borrowed-icon"
              />
            </div>
            <h3 class="tag">BORROWED</h3>
          </button>
          <button class="menu-btn">
            <div>
              <font-awesome-icon
                :icon="['fas', 'circle-exclamation']"
                class="needed-icon"
              />
            </div>
            <h3 class="tag">SUPPLIES NEEDED</h3>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserMenu",
  props: {},
  components: {},
  data() {
    return {
      NavCont: document.querySelector(".nav-cont"),
      returnbox: document.querySelector(".return-box"),
    };
  },
  methods: {
    NavMenu() {
      if (this.NavCont.classList.contains("selected")) {
        this.NavCont.classList.remove("selected");
        this.NavCont.classList.add("dismiss");
        console.log("dismiss");
        this.returnbox.classList.remove("return-box-display");
        this.returnbox.classList.add("return-box-nodisplay");
      } else if (this.NavCont.classList.contains("dismiss")) {
        this.NavCont.classList.remove("dismiss");
        this.NavCont.classList.add("selected");
        console.log("selected");
        this.returnbox.classList.remove("return-box-nodisplay");
        this.returnbox.classList.add("return-box-display");
      } else if (
        !this.NavCont.classList.contains("dismiss") ||
        !this.NavCont.classList.contains("selected")
      ) {
        this.NavCont.classList.add("selected");
        console.log("selected");
        this.returnbox.classList.add("return-box-display");
      }
    },
    runOnMounted() {
      window.addEventListener("resize", () => {
        if (window.innerWidth > 1200) {
          this.NavCont.classList.remove("dismiss");
          this.NavCont.classList.remove("selected");
          this.returnbox.classList.remove("return-box-display");
          this.returnbox.classList.remove("return-box-nodisplay");
        }
      });
    },
  },
  mounted() {
    this.runOnMounted();
  },
};
</script>

<style scoped>
.nav-cont {
  height: 100vh;
  width: 18rem;

  display: flex;
  flex-flow: row;
}
.return-box-display {
  display: display;

  height: 100vh;
  width: 100vw;
  opacity: 0.2;
}
.return-box-nodisplay {
  display: none;

  height: 100vh;
  width: 100vw;
  opacity: 0.2;
}
.back-cont {
  display: none;
  width: 1.5rem;
  height: 100%;
}

.icon {
  width: 90%;
  height: 90%;
}
.user {
  width: 100%;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  overflow: hidden;
  margin-top: 1rem;
}
.user-title {
  color: #ecebf3;
}
.username {
  color: #ecebf3;
}
.user-icon-cont {
  width: 4rem;
  height: 4rem;
  display: flex;
  align-content: center;
  justify-content: center;
}
.user-icon {
  width: 80%;
  height: 80%;
}

.user-info {
  margin-left: 1rem;
  width: 12rem;
  overflow: hidden;
}
.menu-container {
  margin-top: 1rem;
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
}
.tag {
  width: 14rem;
}
.menu-icon {
  width: 1rem;
  height: 1rem;

  border-radius: 2rem;
}
.menu-btn {
  padding: 1rem;
  width: 100%;
  border: none;

  color: white;
  text-decoration: none;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-evenly;
  align-items: center;
  transition: background-color 0.2s linear;
}
.menu-btn:hover {
  background-color: var(--lightblue);
}
.catalog-icon,
.borrowed-icon,
.needed-icon {
  color: #c7d6d5;
  width: 2rem;
  height: 2rem;
}
.open-menu-cont {
  display: none;
  width: 2rem;
  height: 2rem;
}
.open-menu-btn {
  width: 100%;
  height: 100%;
}
.open-menu-btn {
  border: none;
  background-color: transparent;
}
.open-menu-icon-cont {
  width: 100%;
  height: 100%;
}
.open-menu-icon {
  width: 100%;
  height: 100%;
}
/* animations  */
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
/* media query */
/* mobile */
@media (max-width: 1200px) {
  .nav-cont {
    transform: translateX(-100%);
  }
  .open-menu-cont {
    display: block;
  }
}
</style>
