<template>
  <div class="popUpPanel">
    <div class="imagePop">
      <img class="imagePopView" :src="img_link" />
    </div>
    <div class="editPop" v-if="!editMode">
      <button class="editbtn" v-if="!editMode" @click="editToggle">
        <span class="material-symbols-outlined editinfo"> edit </span>
      </button>
    </div>
    <div class="detailsPop">
      <div class="detailsName poprow">
        <div class="text col1">Name</div>
        <div v-if="!editMode" class="text col2 col2name">{{ editname }}</div>
        <div v-if="editMode" class="text col2 col2name">
          <input v-model="editname" />
        </div>
      </div>

      <div class="detailsCat poprow">
        <div class="text col1">Category</div>
        <button
          v-if="!editMode"
          class="text col2 extrabtn arrowbtn"
          @click="categoryInfo"
        >
          {{ listCategoryName[editcategory - 1].name }}
          <div class="heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
        <div v-if="editMode" class="text col2 col2name">
          <select id="Category" v-model="editcategory" required>
            <option disabled value="">Choose a Category</option>
            <option value="1">Tools</option>
            <option value="2">Paint</option>
            <option value="3">Tape</option>
            <option value="4">Wire</option>
            <option value="5">First Aid</option>
            <option value="6">Fabric</option>
            <option value="7">Paper Mache</option>
            <option value="8">Glue</option>
            <option value="9">Sewing</option>
            <option value="10">Miscellaneous</option>
            <option value="11">Coloring Materials</option>
            <option value="12">Sculpture</option>
            <option value="13">Wood</option>
            <option value="14">Craft Supplies</option>
            <option value="15">Foam</option>
            <option value="16">Printmaking</option>
            <option value="17">Paper</option>
            <option value="18">Drawing</option>
            <option value="19">Resin Printer</option>
            <option value="20">3D Printer</option>
            <option value="21">Stained Glass</option>
            <!-- Add other options here -->
          </select>
        </div>
      </div>
      <div class="detailsStock poprow">
        <div class="text col1">Total Stock Available</div>
        <button
          v-if="!editMode"
          class="text col2 extrabtn arrowbtn"
          @click="locationToggle"
        >
          {{ editquantity }}
          <div class="expandbtn heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
        <button
          v-if="editMode"
          class="text col2 extrabtn arrowbtn"
          @click="locationToggle"
        >
          {{ this.editquantity }}
          <div class="expandbtn heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
      </div>
      <div class="detailsLocation" v-if="location">
        <div class="poprow">
          <div class="text col1" id="location">Makerspace</div>
          <div v-if="!editMode" class="text col2" id="locationQ">
            {{ quantity1 }}
          </div>
          <input v-if="editMode" v-model="quantity1" type="number" />
          <input v-if="editMode" v-model="input" type="text" class="input" />
          <button v-if="editMode" @click="updateInput" class="updateBtn">
            Update
          </button>
        </div>
        <div class="poprow">
          <div class="text col1" id="location">Backroom</div>
          <div v-if="!editMode" class="text col2" id="locationQ">
            {{ quantity2 }}
          </div>
          <input v-if="editMode" v-model="this.quantity2" type="number" />
          <input v-if="editMode" v-model="input2" type="text" class="input" />
          <button v-if="editMode" @click="updateInput2" class="updateBtn">
            Update
          </button>
        </div>
      </div>
      <div class="detailsPurchase poprow">
        <div class="text col1">Purchase Link</div>
        <a v-if="!editMode" class="text col2 col2name purchlink" :href="link">{{
          editLink
        }}</a>
        <input v-if="editMode" v-model="editLink" type="text" />
      </div>
      <div class="detailsVendor poprow">
        <div class="text col1">Vendor</div>
        <button
          v-if="!editMode"
          class="text extrabtn col2 arrowbtn"
          @click="vendorInfo"
        >
          {{ listVendorsName[editvendor - 1].name }}
          <div class="heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
        <select v-if="editMode" id="Vendor" v-model="editvendor" required>
          <option disabled value="">Choose a Vendor</option>
          <option value="1">ShopDOE</option>
          <option value="2">Amazon</option>
          <option value="3">Blick</option>
          <option value="4">Home Depot</option>
          <option value="5">Form Labs</option>
          <option value="6">Bambu Lab</option>
          <option value="7">Hobby Lobby</option>
          <option value="8">Fastenal</option>
          <option value="9">Glass Crafters</option>
          <option value="10">Michaels</option>
          <option value="11">Adorama</option>
        </select>
      </div>
      <div class="detailsDate poprow">
        <div class="text col1">Date Last Purchased</div>
        <div v-if="!editMode" class="text col2">{{ editDate }}</div>
        <div v-if="editMode">
          <input v-model="editDate" type="date" />
          <button class="addCurrentDate" @click="addCurrentDate()">
            Add Current Date
          </button>
        </div>
      </div>
      <div>
        <button class="save" v-if="editMode" @click="saveChanges">
          Save Changes
        </button>
      </div>
    </div>
    <div class="logPop">
      <div class="subheading changelog">Inventory Change Log</div>
      <button @click="changeobd" class="text logorg">
        DateTime {{ ascending ? "↓" : "↑" }}
      </button>
      <div id="logs">
        <InvLog />
      </div>
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
    const categoryToFind = this.category;
    const listCategory = [
      { value: 1, name: "Tools", shtName: "TLS" },
      { value: 2, name: "Paint", shtName: "PT" },
      { value: 3, name: "Tape", shtName: "TP" },
      { value: 4, name: "Wire", shtName: "WR" },
      { value: 5, name: "First Aid", shtName: "FA" },
      { value: 6, name: "Fabric", shtName: "FAB" },
      { value: 7, name: "Paper Mache", shtName: "PM" },
      { value: 8, name: "Glue", shtName: "GL" },
      { value: 9, name: "Sewing", shtName: "SE" },
      { value: 10, name: "Miscellaneous", shtName: "MISC" },
      { value: 11, name: "Coloring Materials", shtName: "CM" },
      { value: 12, name: "Sculpture", shtName: "SC" },
      { value: 13, name: "Wood", shtName: "WD" },
      { value: 14, name: "Craft Supplies", shtName: "CS" },
      { value: 15, name: "Foam", shtName: "FM" },
      { value: 16, name: "Printmaking", shtName: "PRTM" },
      { value: 17, name: "Paper", shtName: "PAP" },
      { value: 18, name: "Drawing", shtName: "DR" },
      { value: 19, name: "Resin Printer", shtName: "RES" },
      { value: 20, name: "3D Printer", shtName: "3D" },
      { value: 21, name: "Stained Glass", shtName: "STGL" },
      //add the other categories if their is more
    ];
    const CategoryIndex =
      listCategory.findIndex((category) => category.name === categoryToFind) +
      1;

    const vednorTofind = this.vendor;
    const listVendors = [
      { value: 1, name: "ShopDOE", shtName: "DOE" },
      { value: 2, name: "Amazon", shtName: "AMZ" },
      { value: 3, name: "Blick", shtName: "BLICK" },
      { value: 4, name: "Home Depot", shtName: "HD" },
      { value: 5, name: "Form Labs", shtName: "FL" },
      { value: 6, name: "Bambu Lab", shtName: "BL" },
      { value: 7, name: "Hobby Lobby", shtName: "HL" },
      { value: 8, name: "Fastenal", shtName: "FAST" },
      { value: 9, name: "Glass Crafters", shtName: "GLCRFT" },
      { value: 10, name: "Michaels", shtName: "MIC" },
      { value: 11, name: "Adorama", shtName: "ADO" },
      // ... add other vendors here
    ];
    const VendorIndex =
      listVendors.findIndex((vendor) => vendor.name === vednorTofind) + 1;

    return {
      store: useItemsStore(),
      ascending: true,
      location: false,
      editMode: false,
      editname: this.name,
      editcategory: CategoryIndex + 1,
      listCategoryName: listCategory,
      editquantity: this.quantity,
      quantity1: this.quantM,
      quantity2: this.quantB,
      editLink: this.link,
      editvendor: VendorIndex + 1,
      listVendorsName: listVendors,
      editDate: this.date,
      changes: "",
    };
  },
  methods: {
    findchange() {
      if (this.editname != this.name) {
        this.changes = this.changes + "Name: " + this.editname + " ";
      }
      if (this.listCategoryName[this.editcategory - 1].name != this.category) {
        this.changes =
          this.changes +
          ", " +
          "Category: " +
          this.listCategoryName[this.editcategory - 1].name;
      }
      if (this.quantity1 != this.quantM) {
        this.changes =
          this.changes + ", " + "Makerspace Quantity: " + this.quantity1;
      }
      if (this.quantity2 != this.quantB) {
        this.changes =
          this.changes + ", " + "Backroom Quantity: " + this.quantity2;
      }
      if (this.editLink != this.link) {
        this.changes = this.changes + ", " + "Purchase Link: " + this.editLink;
      }
      if (this.listVendorsName[this.editvendor - 1].name != this.vendor) {
        this.changes =
          this.changes +
          ", " +
          "Vendor: " +
          this.listVendorsName[this.editvendor - 1].name;
      }
  
    },
    changeobd() {
      this.ascending = !this.ascending; // Toggle the state
      this.store.logs.reverse();
    },
    getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length == 2) return parts.pop().split(";").shift();
    },
    saveLogs() {
      let newCategory = "";
      let newVendor = "";
      this.listCategoryName.forEach((element) => {
        if (parseInt(this.editcategory) === element.value) {
          newCategory = element.shtName;
        }
      });
      this.listVendorsName.forEach((element) => {
        if (parseInt(this.editvendor) === element.value) {
          newVendor = element.shtName;
        }
      });
      let logData = {
        name: this.editname,
        category: newCategory,
        backroom_quantity: parseInt(this.editquantity),
        makerspace_quantity: parseInt(this.editquantity),
        // backroom_quantity: parseInt(this.quantity2),
        // makerspace_quantity: parseInt(this.quantity1),
        vendor: newVendor,
        purchase_link: this.editLink,
        pub_date: this.editDate,
        change: this.changes,
        // Add other properties as needed
      };
      const config = useRuntimeConfig();
      fetch(
        `${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/addLog/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.getCookie("csrftoken"),
          },
          body: JSON.stringify(logData),
        }
      )
        .then((response) => response.json())
        .then((data) => {
        })
        .catch((error) => console.error("Error:", error));
    },
    updateInput() {
      const number = parseInt(this.input);
      if (this.input.match(/^[+-]?\d+$/) || this.input == "") {
        this.quantity1 += number;
        if (this.quantity1 < 0) {
          this.quantity1 = 0;
        }
      } else {
        alert("Please enter a number with a + or - sign.");
      }
      this.input = "";
    },
    updateInput2() {
      const number = parseInt(this.input2);
      if (this.input2.match(/^[+-]?\d+$/) || this.input2 == "") {
        this.quantity2 += number;
        if (this.quantity2 < 0) {
          this.quantity2 = 0;
        }
      } else {
        alert("Please enter a number with a + or - sign.");
      }
      this.input2 = "";
    },
    calculateTotalQuantity() {
      return this.quantity1 + this.quantity2;
    },

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
    editToggle() {
      if (!this.editMode) {
        this.editMode = true;
      }
    },
    addCurrentDate() {
      const currentDate = new Date().toISOString().slice(0, 10);
      this.editDate = currentDate;
    },

    changeSize() {
      document.querySelectorAll(".itemMain").forEach((item) => {
        if (
          item.lastElementChild.firstElementChild.textContent === this.editname
        ) {
          item.classList.add("infoFull");
          item.classList.remove("mainSize");
        }
      });
    },

    async saveChanges() {
      this.findchange();
      this.saveLogs();
      const formData = new FormData();
      formData.append("name", this.editname);
      formData.append("category", this.editcategory);
      formData.append("image_url", this.img_link);
      formData.append("makerspace_quantity", this.quantity1);
      formData.append("backroom_quantity", this.quantity2);
      formData.append("purchase_link", this.editLink);
      formData.append("vendor", this.editvendor);
      formData.append("last_purchased", this.editDate);
      this.store.getLogs(this.editname);
      this.store.getLogs(this.editname);

      try {
        const config = useRuntimeConfig();
        const response = await fetch(
          `${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/editItems/${this.store.id}/`,
          {
            method: "PUT",
            mode: "cors",
            cache: "no-cache",
            credentials: "same-origin",
            body: formData,
          }
        );

        const data = await response.json();
        this.store.edit = true;
        this.editMode = false;
      } catch (error) {
        console.log(error);
      }
      const config = useRuntimeConfig();
      const response = await fetch(
        `${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/category/`
      );
      const new_items = await response.json();
      const newresults = new_items.sort((a, b) =>
        a.category_name > b.category_name
          ? 1
          : b.category_name > a.category_name
          ? -1
          : 0
      );
      this.store.$patch({ items: newresults });

      setTimeout(this.changeSize, 5);
    },
  },

  computed: {
    editquantityNew: {
      get() {
        return this.editMode
          ? this.editquantity
          : this.calculateTotalQuantity();
      },
      set(newValue) {
        if (this.editMode) {
          this.editquantity = newValue;
        } else {
          this.$emit("update:quantity1", newValue);
        }
      },
    },
  },
  watch: {
    quantity1(newValue) {
      if (this.editMode) {
        this.editquantity = newValue + this.quantity2;
      }
    },
    quantity2(newValue) {
      if (this.editMode) {
        this.editquantity = this.quantity1 + newValue;
      }
    },
    $props: {
      handler() {
        const listCategory = [
          { value: 1, name: "Tools" },
          { value: 2, name: "Paint" },
          { value: 3, name: "Tape" },
          { value: 4, name: "Wire" },
          { value: 5, name: "First Aid" },
          { value: 6, name: "Fabric" },
          { value: 7, name: "Paper Mache" },
          { value: 8, name: "Glue" },
          { value: 9, name: "Sewing" },
          { value: 10, name: "Miscellaneous" },
          { value: 11, name: "Coloring Materials" },
          { value: 12, name: "Sculpture" },
          { value: 13, name: "Wood" },
          { value: 14, name: "Craft Supplies" },
          { value: 15, name: "Foam" },
          { value: 16, name: "Printmaking" },
          { value: 17, name: "Paper" },
          { value: 18, name: "Drawing" },
          { value: 19, name: "Resin Printer" },
          { value: 20, name: "3D Printer" },
          { value: 21, name: "Stained Glass" },
          //add the other categories if their is more
        ];
        const listVendors = [
          { value: 1, name: "ShopDOE" },
          { value: 2, name: "Amazon" },
          { value: 3, name: "Blick" },
          { value: 4, name: "Home Depot" },
          { value: 5, name: "Form Labs" },
          { value: 6, name: "Bambu Lab" },
          { value: 7, name: "Hobby Lobby" },
          { value: 8, name: "Fastenal" },
          { value: 9, name: "Glass Crafters" },
          { value: 10, name: "Michaels" },
          { value: 11, name: "Adorama" },
          // ... add other vendors here
        ];
        (this.editname = this.name),
          (this.editcategory =
            listCategory.findIndex(
              (category) => category.name === this.category
            ) + 1),
          (this.editquantity = this.quantity),
          (this.quantity1 = this.quantM),
          (this.quantity2 = this.quantB),
          (this.editLink = this.link),
          (this.editvendor =
            listVendors.findIndex((vendor) => vendor.name === this.vendor) + 1),
          (this.editDate = this.date);
      },
      deep: true,
      immediate: true,
    },
  },
};
</script>

<style>
#logs {
  height: 9vw;
}
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
  overflow-x: hidden;
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
}

.col2name {
  padding-right: 5rem;
}

.purchlink {
  width: 30rem;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
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
  background-color: white;
}

.logorg {
  text-align: left;
  width: 100%;
  font-weight: 400;
  /* margin-bottom: 50px; */
}

.input {
  width: 10%;
  margin-left: 10px;
}

.updateBtn {
  width: 55px;
  height: 23px;
  background-color: white;
  color: black;
  font-size: 13px;
  margin-left: 10px;
  border: solid black 1px;
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
  background-color: white;
}

input,
select {
  font-size: clamp(0.5rem, 1rem + 10vw, 1.5rem);
}

.addCurrentDate {
  max-width: 15rem;
  font-size: clamp(0.5rem, 1rem + 10vw, 1.5rem);
  padding: 1rem;
  margin-left: 10px;
  background-color: rgb(217, 217, 243);
  border-radius: 2rem;
}

.save {
  background-color: var(--darkblue);
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.3rem;
  cursor: pointer;
  transition: background-color 0.2s;
  margin: 2rem auto;
  /* Center horizontally */
  display: block;
  font-size: clamp(0.5rem, 1rem + 10vw, 1.5rem);
}

.save:hover {
  background-color: var(--blue);
}

@media screen and (max-width: 768px) {
  .save {
    width: 100%;
    /* Full width on smaller screens */
  }
}

@media screen and (max-width: 375px) {
  .purchlink {
    width: 20rem;
  }
}

@media screen and (max-width: 280px) {
  .popUpPanel {
    overflow-x: scroll;
  }
  .col2 {
    padding-right: 0;
  }
  .extrabtn {
    min-width: min-content;
    width: 50%;
    text-align: left;
  }
}
</style>
