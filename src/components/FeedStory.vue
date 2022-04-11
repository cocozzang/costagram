<template>
  <div class="card">
    <div class="card-body d-flex justfy-content-start">
      <ul class="list-inline mb-0">
        <li class="list-inline-item align-conent-center">
          <button class="btn p-0 m-0">
            <div class="d-flex flex-column align-items-center">
              <div
                class="rounded-circle overflow-hidden d-flex justify-content-conter align-items-center border border-2 border-danger me-2 story-profile-photo"
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
              <small>cat1</small>
            </div>
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "FeedStory",
};
</script>

<style></style>
