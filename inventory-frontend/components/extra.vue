<template>
  <div class="popUpPanel">
    <div class="imagePop">
      <img class="imagePopView" :src="img_link" />
    </div>
    <div class="editPop">
      <button class="editbtn">
        <span class="material-symbols-outlined editinfo"> edit </span>
      </button>
    </div>
    <div class="detailsPop">
      <div class="detailsName poprow">
        <div class="text col1">Name</div>
        <div class="text col2 col2name">{{ name }}</div>
      </div>

      <div class="detailsCat poprow">
        <div class="text col1">Category</div>
        <button class="text col2 extrabtn arrowbtn" @click="categoryInfo">
          {{ category }}
          <div class="heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
      </div>
      <div class="detailsStock poprow">
        <div class="text col1">Total Stock Available</div>
        <button class="text col2 extrabtn arrowbtn" @click="locationToggle">
          {{ quantity }}
          <div class="expandbtn heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
      </div>
      <div class="detailsLocation" v-if="location">
        <div class="poprow">
          <div class="text col1" id="location">Makerspace</div>
          <div class="text col2" id="locationQ">{{ quantM }}</div>
        </div>
        <div class="poprow">
          <div class="text col1" id="location">Backroom</div>
          <div class="text col2" id="locationQ">{{ quantB }}</div>
        </div>
      </div>
      <div class="detailsPurchase poprow">
        <div class="text col1">Purchase Link</div>
        <a class="text col2" :href="link">{{ link }}</a>
      </div>
      <div class="detailsVendor poprow">
        <div class="text col1">Vendor</div>
        <button class="text extrabtn col2 arrowbtn" @click="vendorInfo">
          {{ vendor }}
          <div class="heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
      </div>
      <div class="detailsDate poprow">
        <div class="text col1">Date Last Purchased</div>
        <div class="text col2">{{ date }}</div>
      </div>
    </div>
    <div class="logPop">
      <div class="subheading changelog">Inventory Change Log</div>
      <button class="text logorg">DateTime</button>
    </div>
  </div>
</template>

<script>
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Extra",
  props: {
    img_link: String,
    name: String,
    category: String,
    quantity: Number,
    link: String,
    vendor: String,
    date: String,
    quantM: Number,
    quantB: Number,
  },
  data() {
    return {
      store: useItemsStore(),
      location: false,
    };
  },
  methods: {
    vendorInfo() {
      this.store.$patch({ vendor: true, vendorHeader: true });
      this.store.inactive(".extraTab", ".tab1", ".tab1btn");
      if (this.store.categoryHeader) {
        this.store.inactive(".categoryTab", ".tab3", ".tab3btn");
      }
      this.store.active(".vendorTab", ".tab2", ".tab2btn");
    },
    categoryInfo() {
      this.store.$patch({ categoryPop: true, categoryHeader: true });
      if (this.store.vendorHeader) {
        this.store.inactive(".vendorTab", ".tab2", ".tab2btn");
      }
      this.store.inactive(".extraTab", ".tab1", ".tab1btn");
      this.store.active(".categoryTab", ".tab3", ".tab3btn");
    },
    locationToggle() {
      this.location = !this.location;
      if (this.location === true) {
        document.querySelector(".expandbtn").style.transform = "rotate(90deg)";
      } else {
        document.querySelector(".expandbtn").style.transform = "none";
      }
    },
  },
};
</script>

<style>
.editPop {
  height: 5rem;
  width: 100%;
  display: flex;
  align-items: center;
}
.editbtn {
  height: 4rem;
  width: 4rem;
  margin-left: 5rem;
  border-radius: 3rem;

  background-color: var(--lightblue);
}
.editinfo {
  color: var(--darkblue);
}
#location {
  color: var(--darkergray);
}
#locationQ {
  color: var(--darkestgray);
}
.rightarrow {
  height: 3rem;
  width: 3rem;
  padding-left: 0.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--tpgray);
  border-radius: 2rem;
  color: var(--darkergray);
  transition: all 0.2s;
}
.rightarrow:hover {
  background-color: var(--darkgray);
  color: var(--darkestgray);
}
.rightarrow:active,
.rightarrow:focus {
  background-color: var(--tpdarkgray);
}
.arrowbtn {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  min-width: 100%;
}
.popUpPanel {
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.imagePop {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 20%;
  margin-top: 2rem;
}
.imagePopView {
  max-height: 80%;
  max-width: 80%;
  object-fit: scale-down;
}
.poprow {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 2rem;
  height: fit-content;
  width: 100%;
}
.col1 {
  margin-left: 2rem;
  margin-right: 2rem;
  min-width: 10rem;
  width: 20%;
  color: var(--darkestgray);
}
.col2 {
  width: 70%;
  padding-right: 5rem;
}

.extrabtn {
  min-width: fit-content;
  width: 50%;
  text-align: left;
}

.changelog,
.logorg {
  padding: 1.5rem;
  border-bottom: var(--border);
}
.changelog {
  border-top: var(--border);
}

.logorg {
  text-align: left;
  width: 100%;
  font-weight: 400;
}
.logPop,
.detailsPop,
.imagePop {
  width: 100%;
}
.detailsLocation {
  margin-left: 2rem;
}
.detailsPop {
  min-width: fit-content;
  width: 90%;
}

@media screen and (max-width: 760px) {
  .col2 {
    padding-right: 0;
  }
  .col2name {
    padding-right: 5rem;
  }
}
</style>
