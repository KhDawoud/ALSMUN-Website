<script type="ts">
    import { Link } from "svelte-routing";
    import Construction from "../../assets/Icons/Construction.svg";
    import NavBar from "../Components/NavBar.svelte";
</script>


<NavBar /> 
<div class="flex flex-col items-center justify-center h-screen">
    <div class="flex flex-col md:flex-row items-center p-10 space-y-5 md:space-x-5 bg-gray-100 rounded-xl">
        <!-- Text Section -->
        <div class="w-full md:w-1/2 flex flex-col space-y-3 text-center md:order-1">
            <h1 class="text-7xl font-bold mb-2"> Sorry! </h1>
            <h3 class="text-4xl font-semibold"> Under Construction</h3>
            <hr class="my-3">
            <span class="font-light my-4"> This page is still being built but will be available in the near future. In the meantime, you can check out the rest of the website </span>
            <Link class="bg-blue-500 rounded-xl hover:bg-blue-700 p-3 w-full md:w-1/3 text-white mx-auto " to="/"> Return Home </Link>
        </div>
        <!-- Image Section -->
        <img src={Construction} alt="Work in progress" class="w-full md:w-1/2 mx-auto md:order-2" width="300rem">
    </div>
</div>

