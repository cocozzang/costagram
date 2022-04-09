<template>
  <div
    class="feed wrapper container d-flex justify-content-center"
    style="background-color: #fafafa"
  >
    <div class="col-9">
      <div class="d-flex justify-content-between">
        <h3>회원가입</h3>
        <router-link :to="{ name: 'LoginView' }"><p>로그인</p></router-link>
      </div>
      <form @submit.prevent="submitform">
        <div class="mb-3">
          <label for="username" class="form-label ms-2">ID</label>
          <input
            type="text"
            class="form-control"
            id="username"
            v-model="form.username"
          />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label ms-2">Password</label>
          <input
            type="password"
            class="form-control"
            id="password"
            autocomplete="on"
            v-model="form.password"
          />
        </div>

        <div class="mb-3">
          <label for="nickname" class="form-label ms-2">nickname</label>
          <input
            type="text"
            class="form-control"
            id="nickname"
            v-model="form.nickname"
          />
        </div>

        <div class="mb-3">
          <label for="email" class="form-label ms-2">Email</label>
          <input
            type="email"
            class="form-control"
            id="email"
            v-model="form.email"
          />
        </div>

        <div class="mb-3">
          <label for="first_name" class="form-label ms-2">First name</label>
          <input
            type="text"
            class="form-control"
            id="first_name"
            v-model="form.firs_tname"
          />
        </div>

        <div class="mb-3">
          <label for="last_name" class="form-label ms-2">Last name</label>
          <input
            type="text"
            class="form-control"
            id="last_name"
            v-model="form.last_name"
          />
        </div>

        <div class="mb-3">
          <label for="lastname" class="form-label ms-2">Profile image</label>
          <input
            type="file"
            class="form-control"
            name="profileimage"
            id="profileimage"
            ref="profileimage"
            @change="imageUpload"
          />
        </div>
        <button type="submit" class="btn btn-primary" @click="submitForm">
          Sign up
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignupView",
  data() {
    return {
      form: {
        username: "",
        password: "",
        nickname: "",
        email: "",
        first_name: "",
        last_name: "",
        profileimage: "",
      },
      errors: [],
    };
  },
  methods: {
    submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      const formdata = new FormData();
      formdata.append("username", this.form.username);
      formdata.append("password", this.form.password);
      formdata.append("email", this.form.email);
      formdata.append("nickname", this.form.nickname);
      formdata.append("first_name", this.form.firs_tname);
      formdata.append("last_name", this.form.last_name);
      formdata.append("profile_image", this.form.profileimage);

      const config = {
        headers: {
          "content-Type": "multipart/form-data",
        },
      };

      console.log(formdata.nickname);

      axios
        .post("http://127.0.0.1:8000/auth/users/", formdata, config)
        .then(() => {
          alert("회원가입 됨 ㅇㅇ 0ㅅ0");

          this.$router.push({ name: "LoginView" });
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");
            console.log(JSON.stringify(error));
          }
        });
    },
    imageUpload() {
      this.form.profileimage = this.$refs.profileimage.files[0];
    },
  },
};
</script>

<style></style>
