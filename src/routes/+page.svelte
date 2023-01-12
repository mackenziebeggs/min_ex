<script>
  let response;

  async function postData() {
    try {
      const res = await fetch("http://localhost:8000/endpoint", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      });
      response = await res.json();
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<button on:click={postData}>Submit</button>
