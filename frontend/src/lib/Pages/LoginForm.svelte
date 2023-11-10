<style>
    @import 'tailwindcss/base.css';
    @import 'tailwindcss/components.css';
    @import 'tailwindcss/utilities.css';
</style>

<script lang="ts">
    import { navigate } from 'svelte-routing'
    import LoginBackground from '../../assets/LoginBackground5.jpg'
    let username: string;
    let password: string;
    let isLoading: boolean;

    const handleSubmit = () => {
        isLoading = true;
        setTimeout(() => {
            isLoading = false;
            navigate('/');
        }, 1000);
    };
</script>

<div class="bg-cover bg-no-repeat bg-center" style="background-image: url('{LoginBackground}');">
      <div class="flex min-h-screen justify-center items-center align-middle">
        <div class="bg-white rounded-2xl w-full lg:w-1/3 md:w-2/3 h-[30rem] m-7 mt-8 p-12 shadow-2xl">
            {#if isLoading}
                <h1>Loading...</h1>
            {:else}
                <h1 class="text-center font-semibold text-4xl"> Login </h1>
                <form class="mt-10" on:submit|preventDefault={handleSubmit}>
                    <div class="relative">
                        <input bind:value={username} type="text" class="bg-yellow-200 py-3 px-4 pl-12 block w-full h-12 border-gray-200 shadow-md rounded-lg text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500" placeholder="Username">
                        <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none z-20 pl-4">
                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
                                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                                <style>svg{fill:#c0c0c0;}</style>
                                <path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/>
                            </svg>
                        </div>
                    </div>
                    <div class="relative mt-6">
                        <input bind:value={password} type="password" class="bg-yellow-200 py-3 px-4 pl-12 block w-full h-12 border-gray-200 shadow-md rounded-lg text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500" placeholder="Password">
                        <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none z-20 pl-4">
                            <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
                                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                                <style>svg{fill:#c0c0c0}</style>
                                <path d="M144 144v48H304V144c0-44.2-35.8-80-80-80s-80 35.8-80 80zM80 192V144C80 64.5 144.5 0 224 0s144 64.5 144 144v48h16c35.3 0 64 28.7 64 64V448c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V256c0-35.3 28.7-64 64-64H80z"/>
                            </svg>
                        </div>
                    </div>
                    <button type="submit" class="text-white h-11 w-full bg-blue-500 shadow-lg rounded-lg hover:rounded-2xl transition-all ease-in mt-7"> Submit </button>
                </form>
                <div class="mt-6 text-center">
                    <hr>
                    <h2 class="mt-2">Or Sign In With</h2>
                    <div class="flex justify-center mt-4">
                        <button class="px-4">
                            <svg id="google" xmlns="http://www.w3.org/2000/svg" height="2.5em" viewBox="0 0 488 512">
                            <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                            <style>#google{fill:#ff0000}</style>
                            <path d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z"/>
                            </svg>
                        </button>
                        <button class="px-4">
                            <svg id="facebook" xmlns="http://www.w3.org/2000/svg" height="2.5em" viewBox="0 0 512 512">
                                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                                    <style>#facebook{fill:#0080ff}</style>
                                    <path d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.15 37-96.48 93.67-96.48 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z"/>
                            </svg>
                        </button>
                        <button class="px-4">
                            <svg id="twitter" xmlns="http://www.w3.org/2000/svg" height="2.5em" viewBox="0 0 448 512">
                                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                                <style>#twitter{fill:#000000}</style>
                                <path d="M64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H64zm297.1 84L257.3 234.6 379.4 396H283.8L209 298.1 123.3 396H75.8l111-126.9L69.7 116h98l67.7 89.5L313.6 116h47.5zM323.3 367.6L153.4 142.9H125.1L296.9 367.6h26.3z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            {/if}
        </div>
    </div>
</div>
