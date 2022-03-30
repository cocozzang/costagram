<template>
  <div class="navbar">
    <!-- navbar start -->
    <nav
      class="navbar navbar-expand-lg border-bottom fixed-top"
      style="background-color: #ffffff"
    >
      <div class="container justify-content-center py-1">
        <div
          class="d-flex flex-row justify-content-between align-items-center col-9"
        >
          <a class="nav-brand" href="/">
            <img src="@/assets/insta-logo.png" alt="" loading="lazy" />
          </a>

          <div>
            <form>
              <input
                class="form-control mr-sm-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
            </form>
          </div>

          <div>
            <ul class="list-inline m-0">
              <li class="list-inline-item ms-3">
                <a href="#" class="link-menu">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.5em"
                    height="1.5em"
                    fill="currentColor"
                    class="bi bi-house-door-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5z"
                    />
                  </svg>
                </a>
              </li>

              <li class="list-inline-item ms-3">
                <a href="#" class="link-menu">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.5em"
                    height="1.5em"
                    fill="currentColor"
                    class="bi bi-send"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576 6.636 10.07Zm6.787-8.201L1.591 6.602l4.339 2.76 7.494-7.493Z"
                    />
                  </svg>
                </a>
              </li>

              <li class="list-inline-item ms-3">
                <a href="#" class="link-menu">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.5em"
                    height="1.5em"
                    fill="currentColor"
                    class="bi bi-plus-square"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
                    />
                    <path
                      d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
                    />
                  </svg>
                </a>
              </li>

              <li class="list-inline-item ms-3">
                <a href="#" class="link-menu">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.5em"
                    height="1.5em"
                    fill="currentColor"
                    class="bi bi-compass"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 16.016a7.5 7.5 0 0 0 1.962-14.74A1 1 0 0 0 9 0H7a1 1 0 0 0-.962 1.276A7.5 7.5 0 0 0 8 16.016zm6.5-7.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z"
                    />
                    <path
                      d="m6.94 7.44 4.95-2.83-2.83 4.95-4.949 2.83 2.828-4.95z"
                    />
                  </svg>
                </a>
              </li>

              <li class="list-inline-item ms-3">
                <a href="#" class="link-menu">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="1.5em"
                    height="1.5em"
                    fill="currentColor"
                    class="bi bi-heart"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
                    />
                  </svg>
                </a>
              </li>

              <li class="list-inline-item align-middle ms-3">
                <a href="#" class="link-menu">
                  <div
                    class="rounded-circle overflow-hidden d-flex justify-content-conter align-items-center topbar-profile-photo"
                  >
                    <img
                      src="@/assets/cat1.jpg"
                      style="
                        transform: scale(1.5);
                        width: 100%;
                        position: absolute;
                        left: 0;
                      "
                    />
                  </div>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
    <!-- navbar end -->
  </div>
</template>

<script>
export default {
  name: "NavBar",
  components: {},
};
</script>

<style lang="css">
.topbar-profile-photo {
  width: 1.5em;
  height: 1.5em;
  position: relative;
}

.link-menu {
  color: black;
}
</style>
