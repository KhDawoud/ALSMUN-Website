<script lang="ts">
  import { Link } from "svelte-routing";
  import Dropdown from "./Dropdown.svelte";
  import Logo from '../../assets/Icons/Logo.png'
  import PFP from "../../assets/Icons/Default_pfp.svg";

  let profileDropdown: boolean = false;  
  let mobileMenu: boolean = false;
  let authenticated: boolean = false;
</script>



<nav class="bg-gray-800">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-20 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">

          <!-- Mobile menu button-->
          <button on:click={() => mobileMenu = !mobileMenu} type="button" class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
            <span class="absolute -inset-0.5"></span>
            <span class="sr-only">Open main menu</span>
            <svg class="{!mobileMenu ? "block":"hidden"} h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
            <svg class="{mobileMenu ? "block":"hidden"} h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>


        </div>
        <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">

          <div class="flex flex-shrink-0 items-center">
            <img class="w-16" src={Logo} alt="ALSMUN Logo">
          </div>

          <div class="hidden sm:ml-6 sm:block py-6">
            <div class="flex space-x-4">
              <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
              <Link to='/' class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">Home</Link>
              <Link to='/meet' class="text-md text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 font-medium">Meet the Team of 2024</Link>
              <Dropdown text="Committees and Topics" options={{"Human Rights Council": "/Committees/HRC", "General Assembly": "/Committees/GA", "Economic & Social Council": "/Committees/ECOSOC", "International Court of Justice": "/Committees/ICJ", "Junior Committee": "/Committees/JC", "Security Council": "/Committees/SC"}} dark={true}/>
              <Dropdown text="Archive" options ={{"ALSMUN1":"/Construction", "ALSMUN2":"/Construction"}} dark = {true}/>
    
            </div>
          </div>
        </div>

        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
          <!-- Profile dropdown -->
          {#if authenticated}
            <div class="relative ml-4">
              <div>
                <button on:click={() => profileDropdown = !profileDropdown} type="button" class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                  <span class="absolute -inset-1.5"></span>
                  <span class="sr-only">Open user menu</span>
                  <img class="h-11 rounded-full" src={PFP} alt="">
                </button>
              </div>

              {#if profileDropdown}
                  <div class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                  <!-- Active: "bg-gray-100", Not Active: "" -->
                  <Link to="/" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem" id="user-menu-item-0">Your Profile</Link>
                  <Link to="/" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem" id="user-menu-item-1">Settings</Link>
                  <Link to="/" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem" id="user-menu-item-2">Sign out</Link>
                  </div>
              {/if}
            </div>
          {:else}
              <Link to='/LogIn' class="hidden sm:block bg-blue-500 rounded-xl px-6 py-3  text-white hover:rounded-3xl hover:px-6 transition-all ease-in duration-150">Sign Up</Link>
          {/if}

        </div>
      </div>
    </div>
  
    <!-- Mobile menu, show/hide based on menu state. -->
    {#if mobileMenu}
        <div class="sm:hidden" id="mobile-menu">
            <div class="space-y-2 px-2 pb-3 pt-2">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <div class="block sm:inline-block">
                    <Link to='/' class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">Home</Link>
                </div>
                <div class="block sm:inline-block">
                    <Link to='/meet' class="text-gray-300 hover:bg-gray-700 hover:text-white block rounded-md px-3 py-2 text-base font-medium">Meet The Team of 2024</Link>
                </div>
                <div class="block sm:inline-block">
                    <Dropdown options={{"Human Rights Council": "/Committees/HRC", "General Assembly": "/Committees/GA", "Economic & Social Council": "/Committees/ECOSOC", "International Court of Justice": "/Committees/ICJ", "Junior Committee": "/Committees/JC", "Security Council": "/Committees/SC"}} text="Committees and Topics" dark={true} />
                </div>
                <div class="block sm:inline-block">
                    <Dropdown text="Archive" options={{"ALSMUN1":"/Construction", "ALSMUN2":"/Construction"}} dark={true}/>
                </div>
                <div class="block sm:inline-block">
                    <Link to='/LogIn' class="bg-blue-500 text-white hover:bg-blue-700 hover:text-white block rounded-md px-3 py-2 text-center font-medium">Sign Up</Link>
                </div>
            </div>
        </div>
    {/if}

  </nav>