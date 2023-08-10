<template>
  <div class="form-container">
    <button @click="store.addItems">
      <span class="material-symbols-outlined closeAdd"> close </span>
    </button>

    <form @submit.prevent="submitForm">
      <div class="input-container">
        <label for="item_id">Item ID</label>
        <input id="item_id" type="text" v-model="item_id" placeholder="Enter Item ID" required />
      </div>
      <div class="input-container">
        <label for="name">Name of the Item</label>
        <input id="name" type="text" v-model="name" placeholder="Enter the Name of the Item" required />
      </div>
      <div class="input-container">
        <label class="text">Quantity</label>
        <div class="quantity-inputs">
          <input id="quantity-makerspace" type="number" v-model="makerspace" placeholder="Maker Space Quantity"
            required />
          <input id="quantity-backroom" type="number" v-model="backroom" placeholder="Back Room Quantity" required />
        </div>
      </div>
      <div class="input-container">
        <label for="min_amount">Minimum amount of Items to display alert</label>
        <input id="min_amount" type="number" v-model="min_amount"
          placeholder="Enter Minium amount of Items to display Alert" />
      </div>
      <div class="input-container">
        <label for="location">Location of the Item</label>
        <input id="location" type="text" v-model="location" placeholder="Enter the location of the Item" required />
      </div>
      <div class="input-container">
        <label for="purchase_link">Purchase Link</label>
        <input id="purchase_link" type="text" v-model="purchase_link" placeholder="Purhcase Link" required />
      </div>
      <div class="input-container">
        <label for="Vendor">Vendor</label>
        <select id="Vendor" v-model="vendor" required>
          <option disabled value="">Choose a Vendor</option>
          <option value="1">ShopDOE</option>
          <option value="2">Amazon</option>
          <option value="3">Blick</option>
          <option value="4">Home Depot</option>
        </select>
      </div>
      <div class="input-container">
        <label for="Category">Category</label>
        <select id="Category" v-model="category" required>
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
      <div class="input-container">
        <label for="image_url">Image Url</label>
        <input id="image_url" type="text" v-model="image_url" placeholder="Enter Image Url" />
      </div>

      <!-- image pre view container  -->
      <div class="upload-container relative flex items-center justify-between w-full">
        <div
          class="drop-area w-full rounded-md border-2 border-dotted border-gray-200 transition-all hover:border-blue-600/30 text-center"
          @dragover.prevent="handleDragOver" @dragleave="handleDragLeave" @drop.prevent="handleDrop">
          <label for="file-input" class="block w-full h-full text-gray-500 p-4 text-sm cursor-pointer">
            {{ dropAreaText }}
          </label>
          <input name="file" type="file" id="file-input" accept="image/*" class="hidden" @change="handleFileChange" />
          <!-- Image upload input -->
          <div class="preview-container" :class="{ hidden: !showPreview }">
            <div class="preview-image w-36 h-36 bg-cover bg-center rounded-md cursor-pointer"
              :style="{ backgroundImage: previewImage }" @click="handleImageClick"></div>
            <span class="file-name my-4 text-sm font-medium" v-if="fileName">{{
              fileName
            }}</span>
            <p class="close-button cursor-pointer transition-all mb-4 rounded-md px-3 py-1 border text-xs text-red-500 border-red-500 hover:bg-red-500 hover:text-white"
              @click="handleClose">
              Delete
            </p>
          </div>
        </div>

        <!-- Bigger Image Preview Modal -->
        <div class="modal" v-if="showModal" @click="closeModal">
          <div class="modal-content">
            <img :src="previewImageModal" alt="Bigger Preview" @click="closeModal" />
          </div>
        </div>
      </div>
      <button class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateItemForm",
};
</script>

<script setup>
import { ref } from "vue";
import { useItemsStore } from "~/store/ItemsStore";

// State variables
const store = useItemsStore();
const dropAreaText = ref("Drop your image here or click to browse");
const showPreview = ref(false);
const showModal = ref(false);
const previewImage = ref("");
const previewImageModal = ref("");
const fileName = ref("");
const item_id = ref("");
const name = ref("");
const location = ref("");
const makerspace = ref(0);
const backroom = ref(0);
const min_amount = ref(0);
const vendor = ref("");
const category = ref("");
const purchase_link = ref("");
const image_url = ref("");
let thisfile = ref();

// Functions
function handleDragOver(event) {
  event.preventDefault();
  dropAreaText.value = "Drop your image here";
}

function handleDragLeave() {
  dropAreaText.value = "Drop your image here or click to browse";
}

function handleDrop(event) {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  thisfile = file;
  showPreview.value = true;
  if (file) {
    showPreview.value = true;
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        previewImage.value = `url(${reader.result})`;
        previewImageModal.value = reader.result;
        fileName.value = file.name;
      };
    }
  }
}

function handleFileChange(event) {
  const file = event.target.files[0];
  thisfile.value = file;
  showPreview.value = true;
  if (file) {
    showPreview.value = true;
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        previewImage.value = `url(${reader.result})`;
        previewImageModal.value = reader.result;
        fileName.value = file.name;
      };
    }
  }
}

function handleClose() {
  showPreview.value = false;
  fileName.value = "";
  previewImage.value = "";
}

function handleImageClick() {
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
}

async function submitForm() {
  const formData = new FormData();
  formData.append("item_id", item_id.value);
  if (thisfile.value) {
    formData.append("image_file", thisfile.value);
  }
  formData.append("image_url", image_url.value);
  formData.append("name", name.value);
  formData.append("purchase_link", purchase_link.value);
  formData.append("backroom_quantity", backroom.value);
  formData.append("makerspace_quantity", makerspace.value);
  formData.append("min_amount", min_amount.value);
  formData.append("vendor", vendor.value);
  formData.append("category", category.value);
  formData.append("location", location.value);

  try {
    const response = await fetch("http://127.0.0.1:8000/items/addItems/", {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      body: formData,
    });

    const data = await response.json();
  } catch (error) {
    console.log(error); //need to do error handling
  }
}
</script>

<style scoped>
.closeAdd {
  position: absolute;
  right: 0;
  margin-right: 3rem;
  margin-top: -1.5rem;
  display: block;
  border-radius: 2rem;
  height: 3rem;
  width: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.closeAdd:hover {
  background-color: var(--tpgray);
}

.closeAdd:active {
  background-color: var(--tpdarkgray);
}

.submit-button {
  background-color: var(--lightblue);
  color: var(--darkblue);
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: var(--medblue);
}

.submit-button:active {
  background-color: var(--blue);
  color: var(--darkerblue);
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  max-width: 90%;
  max-height: 90%;
}

.modal img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.upload-container {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.drop-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  border-radius: 0.375rem;
  border: 2px dotted #cbd5e0;
  transition: border-color 0.2s ease;
}

.drop-area:hover {
  border-color: #4299e1;
}

.drop-area label {
  color: #4a5568;
  width: 100%;
  height: 100%;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 500;
  cursor: pointer;
  text-align: center;
}

/* Hidden file input styles */
.hidden {
  display: none !important;
}

/* Preview container styles */
.preview-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.preview-image {
  width: 16rem;
  height: 16rem;
  background-color: #e2e8f0;
  background-size: cover;
  background-position: center;
  border-radius: 0.375rem;
}

.file-name {
  margin-top: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.close-button {
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 2rem;
  padding: 0.25rem 0.75rem;
  border: 1px solid #e53e3e;
  font-size: 1rem;
  color: #e53e3e;
  border-radius: 0.25rem;
}

.close-button:hover {
  background-color: #e53e3e;
  color: #fff;
}

.form-container {
  margin: 0 auto;
  padding: 2rem;
  background-color: #f5f5f5;
  border-radius: 0.5rem;
}

form {
  display: grid;
  gap: 1.5rem;
}

.input-container {
  display: grid;
  gap: 0.5rem;
}

input,
select {
  padding: 0.8rem;
  font-size: 1.6rem;
  border: 1px solid #ccc;
  border-radius: 0.3rem;
}

.quantity-inputs {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.submit-container {
  display: flex;
  justify-content: center;
}

option {
  font-size: var(--h4);
}

@media screen and (max-width: 760px) {
  .form-container {
    min-width: 100vw;
    align-self: flex-start;
    position: fixed;
    height: 100vh;
    left: 0;
    right: 0;
    border: none;
    z-index: 2000;
    overflow-y: scroll;
    margin-bottom: 20rem;
  }
}
</style>
