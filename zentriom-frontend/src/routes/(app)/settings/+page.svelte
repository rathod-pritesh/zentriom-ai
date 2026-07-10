<script>
	import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "$lib/components/ui/card/index.js";
	import { Button } from "$lib/components/ui/button/index.js";
	import { Settings, Check } from "lucide-svelte";

	let selectedTheme = $state("light");
	let selectedModel = $state("granite");
	let notifications = $state({
		email: true,
		inApp: true,
		desktop: false
	});

	let saveStatus = $state(false);

	function handleSave() {
		saveStatus = true;
		setTimeout(() => saveStatus = false, 1500);
	}
</script>

<div class="max-w-4xl mx-auto space-y-6">
	<!-- Theme configuration -->
	<Card class="bg-white border-stone-200 shadow-xs">
		<CardHeader class="border-b border-stone-100">
			<CardTitle class="text-base font-bold text-stone-900 font-sans">Visual Theme</CardTitle>
			<CardDescription class="text-xs text-stone-400 font-sans">Choose how Zentriom interface looks on your browser</CardDescription>
		</CardHeader>
		<CardContent class="p-6">
			<div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
				<button
					onclick={() => selectedTheme = "light"}
					class="p-4 rounded-xl border text-left flex flex-col justify-between h-24 transition-all cursor-pointer outline-none
						{selectedTheme === 'light' ? 'border-[#A16207] bg-[#A16207]/5' : 'border-stone-200 hover:bg-stone-50'}"
				>
					<span class="text-xs font-bold text-stone-900 font-sans">Light Mode</span>
					<span class="text-[10px] text-stone-400 font-sans">Standard default theme</span>
				</button>

				<button
					onclick={() => selectedTheme = "dark"}
					class="p-4 rounded-xl border text-left flex flex-col justify-between h-24 transition-all cursor-pointer outline-none
						{selectedTheme === 'dark' ? 'border-[#A16207] bg-[#A16207]/5' : 'border-stone-200 hover:bg-stone-50'}"
				>
					<span class="text-xs font-bold text-stone-900 font-sans">Dark Mode</span>
					<span class="text-[10px] text-stone-400 font-sans">High contrast night theme</span>
				</button>

				<button
					onclick={() => selectedTheme = "system"}
					class="p-4 rounded-xl border text-left flex flex-col justify-between h-24 transition-all cursor-pointer outline-none
						{selectedTheme === 'system' ? 'border-[#A16207] bg-[#A16207]/5' : 'border-stone-200 hover:bg-stone-50'}"
				>
					<span class="text-xs font-bold text-stone-900 font-sans">System Default</span>
					<span class="text-[10px] text-stone-400 font-sans">Syncs with operating system</span>
				</button>
			</div>
		</CardContent>
	</Card>

	<!-- Model configuration -->
	<Card class="bg-white border-stone-200 shadow-xs">
		<CardHeader class="border-b border-stone-100">
			<CardTitle class="text-base font-bold text-stone-900 font-sans">AI Model Configuration</CardTitle>
			<CardDescription class="text-xs text-stone-400 font-sans">Choose the primary language model powering your Copilot sessions</CardDescription>
		</CardHeader>
		<CardContent class="p-6 space-y-4">
			<div class="space-y-3">
				<button
					onclick={() => selectedModel = "granite"}
					class="w-full p-4 rounded-xl border text-left flex items-start gap-4 transition-all cursor-pointer outline-none
						{selectedModel === 'granite' ? 'border-[#A16207] bg-[#A16207]/5' : 'border-stone-200 hover:bg-stone-50'}"
				>
					<div class="mt-0.5 shrink-0 flex items-center justify-center size-5 rounded-full border border-stone-300 bg-white">
						{#if selectedModel === 'granite'}
							<div class="size-2.5 rounded-full bg-[#A16207]"></div>
						{/if}
					</div>
					<div>
						<h4 class="text-xs font-bold text-stone-900 font-sans flex items-center gap-2">
							IBM Granite 3.0 (8B) <span class="bg-[#A16207]/10 text-[#A16207] text-[8px] font-bold uppercase tracking-wider px-1.5 py-0.5 rounded-full">Primary</span>
						</h4>
						<p class="text-[10px] text-stone-400 font-sans mt-0.5">Optimized locally for coding assistance, grammar corrections, and fast responses.</p>
					</div>
				</button>

				<button
					onclick={() => selectedModel = "llama"}
					class="w-full p-4 rounded-xl border text-left flex items-start gap-4 transition-all cursor-pointer outline-none
						{selectedModel === 'llama' ? 'border-[#A16207] bg-[#A16207]/5' : 'border-stone-200 hover:bg-stone-50'}"
				>
					<div class="mt-0.5 shrink-0 flex items-center justify-center size-5 rounded-full border border-stone-300 bg-white">
						{#if selectedModel === 'llama'}
							<div class="size-2.5 rounded-full bg-[#A16207]"></div>
						{/if}
					</div>
					<div>
						<h4 class="text-xs font-bold text-stone-900 font-sans">Llama 3.1 (70B)</h4>
						<p class="text-[10px] text-stone-400 font-sans mt-0.5">High parameter count model designed for complex system-level architectural reasoning.</p>
					</div>
				</button>

				<button
					onclick={() => selectedModel = "gemini"}
					class="w-full p-4 rounded-xl border text-left flex items-start gap-4 transition-all cursor-pointer outline-none
						{selectedModel === 'gemini' ? 'border-[#A16207] bg-[#A16207]/5' : 'border-stone-200 hover:bg-stone-50'}"
				>
					<div class="mt-0.5 shrink-0 flex items-center justify-center size-5 rounded-full border border-stone-300 bg-white">
						{#if selectedModel === 'gemini'}
							<div class="size-2.5 rounded-full bg-[#A16207]"></div>
						{/if}
					</div>
					<div>
						<h4 class="text-xs font-bold text-stone-900 font-sans">Gemini 1.5 Flash</h4>
						<p class="text-[10px] text-stone-400 font-sans mt-0.5">Multimodal execution engine optimized for speed and large token context analysis.</p>
					</div>
				</button>
			</div>
		</CardContent>
	</Card>

	<!-- Notification Preferences -->
	<Card class="bg-white border-stone-200 shadow-xs">
		<CardHeader class="border-b border-stone-100">
			<CardTitle class="text-base font-bold text-stone-900 font-sans">Notification Preferences</CardTitle>
			<CardDescription class="text-xs text-stone-400 font-sans">Configure when and how you receive workspace alerts</CardDescription>
		</CardHeader>
		<CardContent class="p-6 space-y-4">
			<div class="space-y-3.5">
				<label class="flex items-center gap-3 cursor-pointer select-none">
					<input
						type="checkbox"
						bind:checked={notifications.email}
						class="size-4.5 accent-[#A16207] cursor-pointer"
					/>
					<div>
						<p class="text-xs font-semibold text-stone-850 font-sans">Email summaries</p>
						<p class="text-[10px] text-stone-400 font-sans mt-0.5">Receive weekly metrics reports and LinkedIn performance indicators.</p>
					</div>
				</label>

				<label class="flex items-center gap-3 cursor-pointer select-none">
					<input
						type="checkbox"
						bind:checked={notifications.inApp}
						class="size-4.5 accent-[#A16207] cursor-pointer"
					/>
					<div>
						<p class="text-xs font-semibold text-stone-850 font-sans">In-App notifications</p>
						<p class="text-[10px] text-stone-400 font-sans mt-0.5">Show notifications badges in the workspace header on updates.</p>
					</div>
				</label>

				<label class="flex items-center gap-3 cursor-pointer select-none">
					<input
						type="checkbox"
						bind:checked={notifications.desktop}
						class="size-4.5 accent-[#A16207] cursor-pointer"
					/>
					<div>
						<p class="text-xs font-semibold text-stone-850 font-sans">Desktop push alerts</p>
						<p class="text-[10px] text-stone-400 font-sans mt-0.5">Show alerts outside the browser when processing operations complete.</p>
					</div>
				</label>
			</div>

			<div class="flex justify-end pt-4 border-t border-stone-100">
				<Button onclick={handleSave} class="bg-[#A16207] text-white hover:bg-[#A16207]/90 h-9 px-5 text-xs font-sans cursor-pointer">
					{#if saveStatus}
						<Check class="size-4 mr-2" /> Settings Saved
					{:else}
						Save Preferences
					{/if}
				</Button>
			</div>
		</CardContent>
	</Card>
</div>
