<script lang="ts">
  import NavBar from "./NavBar.svelte";
  import GroupSection from "./GroupSection.svelte";
  import SDG from "C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/SDG.png";

</script>


<NavBar />

<main class="grid grid-flow-row grid-cols-1 space-y-5 p-5">
    <GroupSection header="The Secretariat" link="/home" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={SDG} />
</main>

