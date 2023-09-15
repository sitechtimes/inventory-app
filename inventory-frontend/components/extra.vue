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
        <button v-if="!editMode" class="text col2 extrabtn arrowbtn" @click="categoryInfo">
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
            <!-- Add other options here -->
          </select>
        </div>
      </div>
      <div class="detailsStock poprow">
        <div class="text col1">Total Stock Available</div>
        <button v-if="!editMode" class="text col2 extrabtn arrowbtn" @click="locationToggle">
          {{ editquantity }}
          <div class="expandbtn heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
        <button v-if="editMode" class="text col2 extrabtn arrowbtn" @click="locationToggle">{{ this.editquantity }}
          <div class="expandbtn heading rightarrow">
            <span class="material-symbols-outlined"> navigate_next </span>
          </div>
        </button>
      </div>
      <div class="detailsLocation" v-if="location">
        <div class="poprow">
          <div class="text col1" id="location">Makerspace</div>
          <div v-if="!editMode" class="text col2" id="locationQ">{{ quantity1 }}</div>
          <input v-if="editMode" v-model="quantity1" type="number">
        </div>
        <div class="poprow">
          <div class="text col1" id="location">Backroom</div>
          <div v-if="!editMode" class="text col2" id="locationQ">{{ quantity2 }}</div>
          <input v-if="editMode" v-model="quantity2" type="number">
        </div>
      </div>
      <div class="detailsPurchase poprow">
        <div class="text col1">Purchase Link</div>
        <a v-if="!editMode" class="text col2 col2name purchlink" :href="link">{{ editLink }}</a>
        <input v-if="editMode" v-model="editLink" type="text">
      </div>
      <div class="detailsVendor poprow">
        <div class="text col1">Vendor</div>
        <button v-if="!editMode" class="text extrabtn col2 arrowbtn" @click="vendorInfo">
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
        </select>
      </div>
      <div class="detailsDate poprow">
        <div class="text col1">Date Last Purchased</div>
        <div v-if="!editMode" class="text col2">{{ editDate }}</div>
        <div v-if="editMode"><input v-model="editDate" type="date">
          <button class="addCurrentDate" @click="addCurrentDate()">Add Current Date</button>
        </div>
      </div>
      <div>
        <button class="save" v-if="editMode" @click="saveChanges">Save Changes</button>
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
    const categoryToFind = this.category
    const listCategory = [
      { value: 1, name: 'Tools' },
      { value: 2, name: 'Paint' },
      { value: 3, name: 'Tape' },
      { value: 4, name: 'Wire' },
      { value: 5, name: 'First Aid' },
      { value: 6, name: 'Fabric' },
      { value: 7, name: 'Paper Mache' },
      { value: 8, name: 'Glue' },
      { value: 9, name: 'Sewing' },
      { value: 10, name: 'Miscellaneous' },
      { value: 11, name: 'Coloring Materials' },
      { value: 12, name: 'Sculpture' },
      { value: 13, name: 'Wood' },
      { value: 14, name: 'Craft Supplies' },
      { value: 15, name: 'Foam' },
      { value: 16, name: 'Printmaking' },
      { value: 17, name: 'Paper' },
      { value: 18, name: 'Drawing' }
      //add the other categories if their is more
    ];
    const CategoryIndex = listCategory.findIndex(category => category.
      name === categoryToFind) + 1;

    const vednorTofind = this.vendor
    const listVendors = [
      { value: 1, name: 'ShopDOE' },
      { value: 2, name: 'Amazon' },
      { value: 3, name: 'Blick' },
      { value: 4, name: 'Home Depot' },
      // ... add other vendors here
    ];
    const VendorIndex = listVendors.findIndex(vendor => vendor.
      name === vednorTofind) + 1;

    return {
      store: useItemsStore(),
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
    };
  },
  methods: {
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
        this.editMode = true
      }
    },
    addCurrentDate() {
      const currentDate = new Date().toISOString().slice(0, 10);
      this.editDate = currentDate;
    },
    async saveChanges() {
      const formData = new FormData();
      formData.append("name", this.editname);
      formData.append("category", this.editcategory);
      formData.append("image_url", this.img_link);
      formData.append("makerspace_quantity", this.quantity1);
      formData.append("backroom_quantity", this.quantity2);
      formData.append("purchase_link", this.editLink);
      formData.append("vendor", this.editvendor);
      formData.append("last_purchased", this.editDate);

      try {
        console.log(this.store.id)
        const response = await fetch(`http://127.0.0.1:8000/items/editItems/${this.store.id}/`, {
          method: "PUT",
          mode: "cors",
          cache: "no-cache",
          credentials: "same-origin",
          body: formData,
        });

        const data = await response.json();
        this.store.edit = true
        console.log(this.store.edit)
        console.log(data)
        this.editMode = false
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    editquantityNew: {
      get() {
        return this.editMode ? this.editquantity : this.calculateTotalQuantity();
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
          { value: 1, name: 'Tools' },
          { value: 2, name: 'Paint' },
          { value: 3, name: 'Tape' },
          { value: 4, name: 'Wire' },
          { value: 5, name: 'First Aid' },
          { value: 6, name: 'Fabric' },
          { value: 7, name: 'Paper Mache' },
          { value: 8, name: 'Glue' },
          { value: 9, name: 'Sewing' },
          { value: 10, name: 'Miscellaneous' },
          { value: 11, name: 'Coloring Materials' },
          { value: 12, name: 'Sculpture' },
          { value: 13, name: 'Wood' },
          { value: 14, name: 'Craft Supplies' },
          { value: 15, name: 'Foam' },
          { value: 16, name: 'Printmaking' },
          { value: 17, name: 'Paper' },
          { value: 18, name: 'Drawing' }
          //add the other categories if their is more
        ];
        const listVendors = [
          { value: 1, name: 'ShopDOE' },
          { value: 2, name: 'Amazon' },
          { value: 3, name: 'Blick' },
          { value: 4, name: 'Home Depot' },
          // ... add other vendors here
        ];
        this.editname = this.name,
          this.editcategory = listCategory.findIndex(category => category.name === this.category) + 1,
          this.editquantity = this.quantity,
          this.quantity1 = this.quantM,
          this.quantity2 = this.quantB,
          this.editLink = this.link,
          this.editvendor = listVendors.findIndex(vendor => vendor.
            name === this.vendor) + 1,
          this.editDate = this.date
      },
      deep: true,
      immediate: true,
    }
  },
  mounted() {
    console.log(this.category)
    console.log(this.editcategory)
    console.log(this.vendor, this.editvendor)
  }
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
  margin-right: 5rem;
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
}

input,
select {
  font-size: clamp(.5rem, 1rem + 10vw, 1.5rem);
}

.addCurrentDate {
  max-width: 15rem;
  font-size: clamp(.5rem, 1rem + 10vw, 1.5rem);
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
  font-size: clamp(.5rem, 1rem + 10vw, 1.5rem);
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
</style>
