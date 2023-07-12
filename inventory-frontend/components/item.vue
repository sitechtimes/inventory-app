<template>
  <div class="itemMain" ref="main">
    <div class="image" v-if="info">
      <img class="imageView" :src="image" :alt="name_id" />
    </div>
    <div class="name-avail">
      <div class="name text">{{ name }}</div>
      <div class="name text quantity">{{ quantity }}</div>
      <div class="avail-updated">
        <div class="availability">
          <span class="availY smalltext" v-if="available"
            >Currently Available</span
          >
          <span class="availN smalltext" v-else>Currently Unavailable</span>
        </div>
        <div class="updated smalltext">Last updated: {{ updated }}</div>
      </div>
      <button class="dropdown" @click="clicked"></button>
    </div>
  </div>
</template>

<style scoped>
.itemMain {
  height: 12.5rem;

  width: 28vw;

  background-color: var(--whitebg);
  display: flex;
  flex-direction: row;
  position: relative;
  margin: 1rem;
}
.name-avail {
  width: 70%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.name,
.availability,
.updated {
  padding-left: 1.5rem;
}

.name {
  padding-top: 1.2rem;

  max-height: 6rem;
}
.quantity {
  color: var(--darkgray);
}
.avail-updated {
  height: 50%;

  min-height: 1.5rem;
  display: flex;
  flex-direction: column;
  margin-bottom: 0.75rem;
  justify-content: space-evenly;

  position: absolute;
  bottom: 0;
  height: fit-content;
}
.updated {
  padding-top: 0.2rem;
  padding-bottom: 0.3rem;
}
.availability {
  padding-top: 0.5rem;
  padding-bottom: 0.4rem;
}
.availY {
  color: rgb(53, 199, 155);
}
.availN {
  color: rgb(255, 43, 106);
}

.image {
  max-height: 100%;
  width: 30%;
  padding: 1.5rem;
  color: #b696db;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.4s;
}
.dropdown {
  visibility: hidden;
}
@media screen and (max-width: 575px) {
  .itemMain {
    flex-direction: column;
    height: fit-content;
    padding-bottom: 4.5rem;
    width: 90%;
    max-width: none;
  }
  .name-avail {
    width: 98%;
  }
  .name {
    font-size: var(--h4);
    padding-right: 1rem;
  }

  .dropdown {
    visibility: visible;
    clip-path: polygon(50% 100%, 0 0, 100% 0);
    width: 0.7rem;
    height: 0.6rem;
    position: absolute;
    right: 1.5rem;
    bottom: 1rem;
    border: none;
    background-color: #fbf7e4;
    z-index: 1000;
  }
  .dropdown:hover {
    cursor: pointer;
    background-color: #dfdbd7;
    scale: 1.1;
  }

  .image {
    width: 80%;
    padding-left: 1.5rem;
    padding-bottom: 0.5rem;
    position: relative;
  }
  .imageView {
    height: 90%;
    width: auto;
    position: absolute;
  }
}
</style>

<script>
export default {
  name: "Item",
  props: {
    name: String,
    quantity: Number,
    description: String,
    updated: String,
    available: Boolean,
    image: String,
    name_id: String,
  },
  data() {
    return {
      info: false,
    };
  },
  methods: {
    clicked() {
      console.log("clicked");
      this.info = !this.info;
    },

    infoScreen() {
      if (window.matchMedia("(min-width: 575px)").matches) {
        this.info = true;
      } else {
        this.info = false;
      }
    },
  },
  mounted() {
    this.infoScreen();
  },
};
</script>
